'''fruits=['apple','banana','orange']
print(fruits)
fruits.append('grape')
print(fruits)
fruits.insert(1,'pear')
print(fruits)
print(len(fruits))
print(fruits.index('orange'))
fruits[::2]
print(fruits[::2])   没有首地址限制，没有尾地址限制，步长为2就是没个1个元素打印一个

fruits[0]='strawberry'
print(fruits)
b=fruits.pop(2)

print(fruits)'''



'''list1=['python','c++',12,23,34]
list1.append('go')
list1.append('c#')
print(list1)'''
'''for i in range(len(list1)):
    print(i,list1[i])'''


'''del list1[2]
print(list1)'''

'''a=len(list1)
print(a)'''

'''print('hello ',end='')
print('worild')'''

'''for i in 'python':
    print(i )
for i in 'python':
    print(i,end='')'''

'''list1=[1,2,7,4]
list2=[1,2,4,1]
print(list1<list2)'''  #只要找到一个不一样的就可以判断整个表达式的真假

'''list1=[1,4,2,54,2]
max(list1)
print(max(list1))
min(list1)
print(min(list1))'''


'''list1=(1,2,3,4)
print(list1)
a=list(list1)
print(a)'''

'''list1=[1,2,3,4,5,4,2,4,1]
list1.count(4)
print(list1.count(4))
list2=[6,7,8,9,10]
list3=['a','b']
list1.extend(list2)
list1.extend(list3)   #extenf将多个列表组合在一起
print(list1)'''

'''list1=['pyhon','java','c++','c#','go','sc','arr']
list1.index('java')
print(list1.index('go',2,5))''' #从第2哥元素查找到第5哥元素，左闭右开区间，go正好在4的索引位置

'''list1=['python','java','c++']
list1.insert(1,'go')
list1.insert(1,'c#')
print(list1)'''

'''list1=['python','java','c++']
a=list1.pop(1)
print(a)
print(list1)
list1.remove('c++')
print(list1)
list1.append('java')
list1.append('c++')
list1.reverse()
print(list1)'''

list1=[1,3,5,8,2,4]
list1.sort(reverse=False)  #True是降序，False是升序（默认）
print(list1)








