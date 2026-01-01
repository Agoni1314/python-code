a=()
print(type(a))
b=tuple()
print(type(b))
#初始值
a=(1,2,3,4)
print(a)
a=(1,'hello','d',[])
print(a)
#通过下标访问
a=(1,2,3,4,5)
print(a[1])
print(a[-1])
#print(a[100])
#切片
a=[1,2,3,4,5,6,7,8,9,10]
print(a[1:3])
print(a[1:9:3])
print(a[-1:1:-3])
for i in a:
    print(i)
for i in range(len(a)) :#默认从0开始遍历
    print(a[i])
#使用in判断是否有元素
a=(1,2,3,4,5)
print(1 in a)
#使用index查找下标
print(a.index(3))
#元祖不能实现增删查改
a=(1,)*10
print(a)

tup=(1,1.2,'python',(5,6,7),[1,2,3,'java'],{'c++','c#'})
tup[4][2]=666
print(tup)
for item,value in enumerate(tup):#会返回一个迭代器，每次迭代产出 (索引, 对应元素) 的元组
    print(item, value)
    if item == 3:
        print(tup[item])
