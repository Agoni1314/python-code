'''name={'1':'python','2':'java','3':'c++'}
print(name)

sudent=dict(p='python',grade=90)  #相当于强制转换
print(sudent)

sc=dict(zip(['name','age'],['张三','13']))
print(sc)'''
#创建字典的三种方式



'''student={'name':'张三','age':'18','性别':'男'}
student['age']=120           
print(student['age'])                         修改
student.update(age=230)
print(student.get('age'))'''


'''student={'name':'张三','age':'18','性别':'男'}
del student['name']
print(student)
del student['性别']                           删除
print(student)'''

'''student={'name':'张三','age':'18','性别':'男'}'''
'''if 'name' in student:
    print(student['name'])
else:
    print('值不存在')'''

'''for key in student.keys():    返回所有的键
    print(key)'''

'''for value in student.values():   返回所有的值
    print(value)'''

'''for items in student.items():   返回所有的键和值组成的队
    print(items)'''

'''for key,value in student.items():
    print(key,value)'''

'''student={'张三':'80','李四':'85','王五':'95'}
student['赵六']=90
print(student)
student.update(李四=60)
print(student)
del student['王五']
print(student)

if '小明' in student:
    print('找到')
else:
    print('没有此人')
print(student)'''



import pprint
student={'1001': {'name':'张三','age':12,'score':{'c':99,'m':97,'e':96}},'1002':{'name':'李四','age':'13','score':{'c':94,'m':89,'e':79}}}
'''pprint.pprint(student)
print(student['1001']['name'],"数学",student['1001']['score']['m'])'''


'''for value in student['1001']['score'].values():'''

'''for value in  student.values():
    sum = 0
    math=value['score']['m']
    chinese = value['score']['c']
    english = value['score']['e']
    sum+=math+chinese+english
    lent=len(value['score'])    #求平均值
    print(sum/lent)'''



import pprint
students= { '1001': {'name': '张三','age': 18,'scores': {'math': 85, 'english': 92, 'python': 88} },
           '1002': { 'name': '李四','age': 19,'scores': {'math': 90, 'english': 85, 'python': 95}}}
#
for value in students.values():  #方法一
    stu_sum = 0
    math=value['scores']['math']
    english=value['scores']['english']
    python=value['scores']['python']
    stu_sum+=math+english+python
    length=len(value['scores'])
    print(stu_sum/length)

for key,value in students.items(): #方法二
    list_stu=list(students[key]['scores'].values())
    print(list_stu)
    print(sum(list_stu)/len(list_stu))

'''sum1=0
for value in students['1001']['scores'].values(): #方法三
    print(value)
    sum1+=value
print(sum1/len(students['1001']['scores']))'''

