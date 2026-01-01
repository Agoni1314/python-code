#使用open打开文件
f=open('h:/test.txt','w')
f.write('111\n')
f.close()

f=open('h:/test.txt','a')
f.write('计算机科学技术和软件工程技术')
f.close()
