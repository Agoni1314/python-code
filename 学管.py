s = {}

def add():
    i = input("学号：")
    if i in s:
        print("已存在！")
        return
    n = input("姓名：")
    e = float(input("英语："))
    m = float(input("数学："))
    p = float(input("Python："))
    s[i] = {"n": n, "sc": {"english": e, "math": m, "python": p}}
    print("添加成功")

def delete():
    i = input("删学号：")
    if i in s:
        del s[i]
        print("删除成功")
    else:
        print("不存在！")

def mod():
    i = input("改学号：")
    if i not in s:
        print("不存在！")
        return
    c = input("科目(english/math/python)：")
    if c in s[i]["sc"]:
        ns = float(input("新分："))
        s[i]["sc"][c] = ns
        print("修改成功")
    else:
        print("科目错")

def qry():
    i = input("查学号：")
    if i in s:
        t = s[i]
        print(f"学号{i} 姓名{t['n']} 英{t['sc']['english']} 数{t['sc']['math']} Py{t['sc']['python']}")
    else:
        print("不存在！")

def sta():
    if not s:
        print("无数据！")
        return
    es = [t["sc"]["english"] for t in s.values()]
    ms = [t["sc"]["math"] for t in s.values()]
    ps = [t["sc"]["python"] for t in s.values()]
    def gs(lst): return (sum(lst)/len(lst), max(lst), min(lst))
    print(f"英：{gs(es)[0]:.2f}/{gs(es)[1]}/{gs(es)[2]} 数：{gs(ms)[0]:.2f}/{gs(ms)[1]}/{gs(ms)[2]} Py：{gs(ps)[0]:.2f}/{gs(ps)[1]}/{gs(ps)[2]}")

def fai():
    if not s:
        print("无数据！")
        return
    for i, t in s.items():
        for c, sc in t["sc"].items():
            if sc < 60:
                print(f"学号{i} 姓名{t['n']} 科目{c} 分{sc}")
                break

def all():
    if not s:
        print("无数据！")
        return
    for i, t in s.items():
        print(f"学号{i} 姓名{t['n']} 成绩{t['sc']}")

while True:
    print("\n1-增 2-删 3-改 4-查 5-统 6-不及格 7-全 0-退")
    cmd = input("选：")
    if cmd == "1": add()
    elif cmd == "2": delete()
    elif cmd == "3": mod()
    elif cmd == "4": qry()
    elif cmd == "5": sta()
    elif cmd == "6": fai()
    elif cmd == "7": all()
    elif cmd == "0": print("再见"); break
    else: print("无效")