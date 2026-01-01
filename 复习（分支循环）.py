'''a,b=map(int,input("请输入两个数").split(" "))
if a>b:
    print("a大")
elif a<b:
    print("b大")
else:
    print("一样大")'''

'''a,b=map(int,input("请输入两个数").split(" "))
if a>0 and b>0:          #"|和&"是二进制运算，对二进制数进行运算,python中的逻辑判断是or和and
    print("都大于0")
elif a>0 or b>0:
    print("任意一项大于0")
else:
    print("都不大于0")'''

'''a=int(input("请输入一个数:")) #input默认输入的值全转化为字符串类型
match a:
    case 1:
        print("是1")
    case 2 | 3:  #在match-case分支中表示或用“|”,分支中没有匹配多个多个模式就没有与运算
        print("2或者3的任意一个")
    case 4:
        print("是4")
    case _:
        print("没有")'''


'''for i in range(1,101):
    print(i)
    i=i+1'''

'''for a in range(100,-1,-1):
   print(a)'''

'''for a in range(100,-2,-2):
    if a==50:
        continue
    print(a)'''

'''for a in 'hello world!':
    print(a)'''

'''list=[12,23,34,45,56]
for a in list:
    print(a)'''

'''a=[12,13,14,15,16]
jishu=[]
oushu=[]
for i in a:
    if i%2==0:
       oushu.append(i)
    else:
        jishu.append(i)
print(oushu)
print(jishu)'''

'''a=10
while a>0:
    print(a)
    a=a-1'''

'''a=0
while a>=0:
    print(a)
    a=a+1
    if a==100:
        break
print(a)'''

'''a=[11,12,13,14,15]
jishu=[]
oushu=[]
while a:
    num=a.pop()
    if num%2==0:
        oushu.append(num)
    else:
        jishu.append(num)
print(jishu)
print(oushu)'''












