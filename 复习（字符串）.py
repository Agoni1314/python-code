'''a='abcdefgc'
print('a' in a)
print('a' not in a)
print(a.count('c'))
print(a.find('e'))#find找不到就返回-1
print(a.index('g'))#index找不到就报错'''

'''name='天亮了-张三.MP3'
a=name.find('-')
b=name.index('.')
c=name[0:a]
d=name[a+1:b]
e=name[b+1:]
print(d+'-'+c+'.'+e)'''

'''a='1-2-3-4-5'.split('-')
print(a)
b='1-2-3-'.split('-')
print(b)
c='-'.join('abc')
print(c)
d='#'.join('1-2-3')
print(d)'''

'''a='abcdefg'.upper()
print(a)
b='ABCDEFG'.lower()
print(b)
c='123abc'.replace('a','4',3)
print(c)'''

'''print('hello \
world!')'''

'''print('i\tam\tstudent')
print('hello\\world!')
print(r'in\nsrc')#当有r的时候就是一种特殊的字符串，其中的转义字符不会被执行，会当作字符串的一部分
a=123.346#python中是超过5(不包含5)才四合五入
print('%.2f' %a)
a=['i','am','student']
print(','.join(a))'''

'''a='i\nam\na\nstudent'
print(a[1:3])
print(a.split())
print(a.split(',',1))'''

'''a='hello world!'
b=a.count('l',2,len(a))
print(b)'''

'''a='hello world!'
b=a.replace('l','s',2)#表示最多不能超过2次（包含2次）
print(b)'''

'''a='hello world!'
b=a.startswith('l',3,100)
print(b)'''

'''a='hello world!'
print(a.endswith('hello',0,5))'''

'''a='dhello world!'
print(a.strip('d'))
a='             hello world!'
print(a.strip())'''

#物联网传感器分析

'''a='AA#+023.8#70%#1#100#BB'
if a[:2]=='AA':
    s1=a.split('#')
    print(s1)
    s2=s1[1]
    s3=s1[2]
    print(s2,s3)
    if s1[3]=='1':
        print('有人')
    else:
        print('没人')
    if s1[4][0]=='1':
        print('1号灯开')
    else:
        print('1号灯关')
    if s1[4][1]=='1':
        print('2号灯开')
    else:
        print('2号灯关')
    if s1[4][2]=='1':
        print('3号灯开')
    else:
        print('3号灯关')'''

'''题目：学生信息格式处理与分析
​任务描述：​学生信息字符串，需要完成以下处理和分析任务：
student1 = "  张三,Python成绩:95,数学成绩:87,英语成绩:92  “
•去除 student1 的首尾空格
•逗号分割学生信息
•查找第一个"成绩"的位置
•查找最后一个"成绩"的位置
•统计 student1中“成绩"出现的次数
•检查学生姓名是否以"张"开头
•检查学生信息是否以数字结尾
•将student1 "成绩"替换为"分数“,限制替换次数为 2 次'''

'''student1 = "     张三,Python成绩:95,数学成绩:87,英语成绩:92    "
a=student1.strip()
print(a)
print(a.split(','))
print(a.find('成绩'))
print(a.rfind('成绩'))
print(a.count('成绩'))
print(a.startswith('张',0,len(student1)))
print(a.endswith('2'))
print(a.replace('成绩:','分数:',2))'''

# !/usr/bin/python
# -*- coding: UTF-8 -*-

'''import re
print(re.match('hello','hello world!').span())
print(re.match('wolrd','hello world!'))'''#只匹配是否是起始位置，如果是就可以用span，如果不是而使用span会报错







