'''a=[1,2,3,4]
a.extend([5,6,7,3])#括号里面要加方括号
print(a)
a.remove(3)#删除第一个值为3的元素
print(a)
#print(a.clear())#清空列表
a.sort()#正序排序
print(a)'''


'''b=(1,1.2,[2,3,4,5,6],{'姓名':'张三','性别':'男'})
print(b[3]['姓名'])
for item,value in enumerate(b):
    print(item,value)'''

'''a={'姓名':'张三','性别':'男','成绩':95}
a['姓名']='李四'
print(a)

for key in a:
    print(key,a[key])
print(a.keys())
print(a.values())
print(a.items())

for key,value in a.items():
    print(key,value)
if '姓名'in a:#根据键去寻找值
    print(a['姓名'])
else:
    print('没有')
student={'1001': {'name':'张三','age':12,'score':{'c':99,'m':97,'e':96}},'1002':{'name':'李四','age':'13','score':{'c':94,'m':89,'e':79}}}
print(student['1001']['name'],'数学',student['1001']['score']['m'])
for key in student:
    print(key,student[key])
    chinese = student['1001']['score']['c']
    math = student['1001']['score']['m']
    english = student['1001']['score']['e']
    sum = chinese + math + english
    # lens=len(student['1001']['score'])
    lent = len(value['score'])
    # lent=len(value['score'])
    print(sum / lent)'''

a={1,2,3,4,5}
print(type(a))
b=set([1,2,3,4])
print(type(b))
a.add(6)
print(a)
a.discard(3)#remove
print(a)
b.pop()
print(b)
for i in a:
    print(i)





