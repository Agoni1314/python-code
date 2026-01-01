a=12
print(type(a))
b='hello world!'
print(type(b))
c=3.14
print(type(c))
d=123
print(type(d))
d=float(d)
print(type(d))
e=3.145
f=str(e)
print(type(f))
#整数字符互转
g=97
g=chr(g)
print(g)
print(ord('d'))
print(chr(104))

print(hex(100)) #十六进制
print(oct(24)) #八进制


#习题
hight,weight,age=map(int,input("请输入身高体重年龄：").split(' '))
a=input("请输入你的运动系数:")
sc=(655+(9.6*float(weight))+(1.8*(hight))-(4.7*age))*float(a)
print(f'最终值{sc:.3f}') #“:”用来区分要格式化的内容和格式化规则
print('0为每个苹果[83]大卡；1为每个芒果[100]大卡；2为每个橙子[50]大卡')
b=int(input('请输入:'))
food=[83,100,50]
num=sc/food[b] #相当于数组的下标
print(f'每天只能吃: {num:.0f}')