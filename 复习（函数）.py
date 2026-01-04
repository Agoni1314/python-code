'''def add(x,y):
    x=10
    y=20
    return x+y

if __name__=='__main__':
   a= add(1,2)
   print(a)'''
'''def canshu(b):
    b='曾安培'
    print(f'你好{b}')
if __name__=='__main__':
    a=input('请输入名字')
    canshu(a)
    print(f'你好{a}')'''
'''def chuancha(b):
    b[0]=100
    b[1]=200
    return b
if __name__=='__main__':
    a=[1,2,3,4]
    chuancha(a)
    print(a)'''

'''def chuancan1(a,b):
    return a+b
def chuancan2(a,b):
    return a+b
if __name__=='__main__':
    R1=chuancan1(1,2)
    print(R1)
    R2=chuancan2(3,4)
    print(R2)'''

'''a=10
b=20
def chuancan():
    a=1
    b=2
    print(a+b)
if __name__=='__main__':
    chuancan()
    print(a+b)'''
'''def chuancan(b,a):
    print(b,a)
if __name__=='__main__':
    chuancan(a=1,b=2)'''

'''def chuancan(b,a=2):
    print(b,a)
if __name__=='__main__':
    chuancan(1)'''
'''def all(*p):
    sum=0
    for i in p:
        sum=sum+i
    return sum

if __name__=='__main__':
    print(all(1,2,3))
    print(all(100,200,300,400))'''
def a(**p):
    for key,value in p.items():
        print(key,p[key])

if __name__=='__main__':
    a(name='张三',age=18,sec='男')
