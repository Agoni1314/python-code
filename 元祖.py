'''tup=(1,) #当元祖只有一个元素的时候要加逗号
tup=(1,2,3,4,5)
print(tup[2])
print(tup[2:4])'''

'''tup1=(1,2,3,4,5)
tup2=(6,7,8,9,10)
tup3=tup1+tup2
print(tup3)
del tup3
print(tup3)'''  #删除完元祖后输出会报错


'''tup1=(1,2,3,4)
len(tup1)
print(len(tup1))
tup2=(1,)*4
print(tup2)
tup3=(1,2,3)
print(1 in tup3)
print(4 in tup3)
for i in (1,2,3,4,5):
    print(i)
    '''
'''tup=(1,1.2,'python',(5,6,7),[1,2,3,'java'],{'c++','c#'})
tup[4][2]=666
print(tup)
for item,value in enumerate(tup):
    #print(item, value)
   if item==3:
       print(tup[item])'''


'''id=[1,2,3]
name=['c++','java','python']
sc=['底层开发','后端开发','ai智能']  解压缩
for i,j,g in zip(id,name,sc):
    print(i,j,g)'''