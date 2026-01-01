#print(*(map(int,input("请输入几个数").split(" "))))
'''a = map(int, input("请输入几个数").split(" "))
print(*a)'''  # 解包迭代器，直接输出数字
#split里面是空格或逗号需要再输入的时候用来分隔，不然会报错
a = list(map(int, input("请输入几个数").split(" ")))
print(a)