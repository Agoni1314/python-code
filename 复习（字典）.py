a={}
print(type(a))
b=dict()
print(type(b))

a={'姓名:':'张三','性别':'男'}#姓名就是键，内容就是值，键识别唯一的
print(a)
print('姓名:' in a)#只能判断key是否存在，和value无关，无法用value in……
print('姓名:' not in a)
print('666' in a)
print('666' not in a)
#使用[]来根据key获取value,无法使用value来查找key
print(a['姓名:'])
#增加键值对
a['成绩：']=90
print(a)
#根据key修改value
a['成绩：']=666
print(a)
#使用pop删除键值对
a.pop('成绩：')
print(a)
#遍历
for key in a:
    print(key,a[key])
print(a.keys())
print(a.values)
print(a.items())
for key,value in a.items():
    print(key,value)

#题
'''任务：创建一个字典students，目前3个学生（姓名:成绩），如表所示，然后完成以下操作：

1.新增一个学生(赵六，90)。
2.修改李四的成绩为70。
3.删除学生王五。
4.查询班级里是否有“小明”这个学生。
5.打印出所有学生的姓名和成绩。'''
students={'张三':'89','李四':'97','王五':'76'}
students['赵六']=90
print(students)
students['李四']=70
students.pop('王五')
print(students)
print('小明' in students)
print(students)
for key in students:
    print(key,students[key])
for key,value in students.items():
    print(key,value)
print(students)
if '李四' in students:
    print(students['李四'])
else:
    print('没有')

import pprint
student={'1001': {'name':'张三','age':12,'score':{'c':99,'m':97,'e':96}},'1002':{'name':'李四','age':'13','score':{'c':94,'m':89,'e':79}}}
print(student['1001']['name'],'数学',student['1001']['score']['m'])
for value in student.values():
    chinese=value['score']['c']
    math=value['score']['m']
    english=value['score']['e']
    sum=0;
    sum=chinese+math+english
    lent=len(value['score'])
    print(sum/lent)



