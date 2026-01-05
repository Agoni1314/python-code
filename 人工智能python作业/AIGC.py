import argparse
import requests
import urllib.parse
import re
import os
import sys


def generate_image(prompt, output_path):
    # 处理输出文件名（如果未指定则自动生成）
    if not output_path:
        # 清理prompt中的特殊字符用于文件名
        safe_prompt = re.sub(r'[^\w\s]', '', prompt)  # 移除标点符号
        safe_prompt = safe_prompt.replace(' ', '_')  # 空格替换为下划线
        safe_prompt = safe_prompt[:30]  # 限制最大长度
        output_path = f"{safe_prompt}.jpg"

    # 确保输出目录存在
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    # 构建请求URL（对prompt进行URL编码）
    encoded_prompt = urllib.parse.quote(prompt)
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"

    try:
        # 发送请求获取图片
        response = requests.get(url, timeout=30)
        response.raise_for_status()  # 检查HTTP错误状态

        # 保存图片到本地
        with open(output_path, 'wb') as f:
            f.write(response.content)

        print(f"✅ 图片已成功保存至: {os.path.abspath(output_path)}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"❌ 请求失败: {str(e)}", file=sys.stderr)
    except IOError as e:
        print(f"❌ 保存文件失败: {str(e)}", file=sys.stderr)

    return False


if __name__ == "__main__":
    # 设置命令行参数解析
    parser = argparse.ArgumentParser(description='使用pollinations.ai生成图片并保存到本地')
    parser.add_argument('prompt', help='生成图片的描述文本（例如："a red cat sitting on a chair"）')
    parser.add_argument('-o', '--output', help='输出文件路径（可选，默认根据prompt生成）')

    args = parser.parse_args()

    # 执行生成操作
    generate_image(args.prompt, args.output)