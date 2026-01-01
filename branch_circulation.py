#s=int(input("输入成绩 "))
#if s>=90:
 #       print("A")
#elif s>80 and s<=89:

 #       print("B")
#elif  s>=70 and s<80:

 #       print("C")
#elif s>=60 and s<70:
 #       print("D")
#elif s<60:
 #       print("E")
#s,a=list(map(int,(input("输入成绩 ").split())))
#print(s+a)
#r,un,th=input("请输入是否有雨，是否有伞，温度").split()
#if r=="是":
 #   if un=="有伞":

  #      print("外出")
   # else:
  #      print("在家")
##else:
 ##          if(float(th)>=30):
  #             print("在家")
   #        else:
    #           print("外出")
'''print('1.出石头。2.出剪刀。3.出布')
computer=1
user=int(input('请出示你的选择'))
if(user==1)and(computer==2)or(user==2)and(computer==3)or(user==3)and(computer==1):
    print('用户获胜')
elif(user==computer):
        print('平局')
else:
        print('计算机获胜')'''


'''a=1
b=2
c=a if a>b else b
print(c)
'''

'''
i=1
r=0
while i<=100:
   if i%2==0:
       r=r+i
   i=i+1
print(r)
'''


'''a=1
b=0
for a in range(101):
   if(a%2==0):
       b = b +a
a=a+1
print(b)
'''


'''name,age,helish=map(int,input('请输入信息').split(','))

print(name,age,helish)
'''


list=input().split(',')
m=list[0]
l=list[1]
f=list[2]
print(m,l,f)