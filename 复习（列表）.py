'''a=[1,2,3,4]
print(type(a))
b=[1,'hello',True,[1,2.3]]#True是python内置的特殊值，加上引号就是字符串了
print(b)
c=[1,'hello','True',[1,2.3]]
print(c)
#使用下标访问元素
d=[1,'hello',[2,3,4]]
print(d[2])
print(len(d))
d[1]='world'
print(d)
#使用负数访问下标
e=[1,2,3,4,5]
print(e[-1])#使用负数就相当于表示倒数第几位
print(e[-2])
#切片操作
f=[1,2,3,4]
print(f[1:3])    #切片操作中，[]里面的两个数字表示一段区间
                  # 取到下标为1到3的元素，包含1，不包含3
#使用切片省略边界
g=[1,2,3,4]
print(g[1:])#省略后边界表示从开始位置一直取到整个列表结束
print(g[:2])#省略前边界，从下标为0开始取，直到结束
#切片下标也可以是负数
print(g[:-1])
#省略两边
print(g[: ])'''
#指定步长
'''h=[1,2,3,4,5,6,7,8,9,10]
print(h[::2])#这里多加一个冒号和一个数字，每隔两个元素
             #（当前的元素和下一个元素才表示两个）取一个元素
print(h[1:-1:2])
#步长还可以是负的，表示从后往前取,输出也是从后往前
print(h[1:9:-2])#起始位置是从左往右，但是步长是从右往左，所以会出现空列表
#改
print(h[1:9:2])
print(h[-1:1:-2])
#当切片范围超出访问下标时，就会尽可能把符合条件的元素取出来
print(h[1:100])
#遍历列表
i=[1,2,3,4,5]
for a in i:
    print(a)
for b in range(0,len(i)):
    #print(i[b])#下标
    i[b]=i[b]+10
print(i)
'''

a=[1,2,3,4,5]
a.append(6) #这里的append不是按照单独的函数使用
a.append('hello')
print(a)
#使用insert在任意位置插入
a.insert(1,'world')  #两个参数，一个是插入的位置，一个是插入的内容
print(a)
a.insert(100,'sc')  #当插入的数据位置大于列表总大小时候就替换最后一个数据
print(a)
#使用in来判断某个元素是否在列表中存在
b=[1,2,3,4,5]
print(10 in b) #返回逻辑值
print(10 not in b)
#使用index方法来判断当前元素在列表什么位置，得到一个下标
print(b.index(2))
#print(b.index(10)) #这样会报错

 #删除操作
 #使用pop删除最后一个元素和任意一个元素
c=[1,2,3,4,5]
c.pop()
print(c)
c.pop(1)
print(c)
#使用remove可以按照值来进行删除
d=['aa','bb','cc','dd']#这样会自动遍历列表
d.remove('cc')
print(d)
#列表拼接
e=[1,2,3,4]
f=[5,6,7,8]
g=e+f
print(g)
#使用extend来进行拼接，这个拼接是把最后一个列表的内容拼接到前一个列表里面
c=e.extend(f)
print(c)#返回None，表示什么都没有，相当于c中的NULL
#使用+=
e+=f
print(e)

#题目
'''题目 1：基本名单管理​
​创建列表​：创建一个列表 fruits，包含以下水果：'apple', 'banana', 'orange'。
​增加元素​：
使用 append()方法在列表末尾添加 'grape'。
使用 insert()方法在 'banana'后面插入 'pear'。
​查询元素​：
打印列表的长度。
查找 'orange'在列表中的位置（索引）。
取出索引为偶数的所有元素。
​修改元素​：将列表中的 'apple'改为 'strawberry'。
​删除元素​：
删除 'banana'。
删除并返回列表的最后一个元素。'''

fruits=['apple','banana','orange']
fruits.append('grape')
fruits.insert(2,'pear')
print(fruits)
print(len(fruits))
print(fruits.index('orange'))
for i in range(0,len(fruits)):
    if i%2==0:
        print(fruits[i])
        i=i+1
fruits[0]='strawberry'
print(fruits)
fruits.pop(1)
print(fruits)
print(fruits[-1])

a=[1,2,3,4]
b=[5,6,7,8]
a.extend(b)
print(a)
print(a<b)
print(a.index(2,1,4))#返回原列表的下标
a.reverse()#倒序输出
print(a)
a.sort(reverse=True)#True是降序，False是升序（默认）
print(a)
e=[1,2,3,4]
print(e[:-2])