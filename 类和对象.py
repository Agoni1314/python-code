'''class Shoes:
    brand='舒适派'
    _sale_price=80
    #__sales_volum=500
    def shoes_info(self):
        print(f'品牌{self.brand}')
        print(f'批发价{self._sale_price}')
        print(f'销量{self.__sales_volum}')
pants=Shoes()
print(pants.brand)
print(pants._sale_price)
#print(pants._sales_volum)
pants.shoes_info()'''



'''创建一个父类Shape，包含属性颜色和方法get_area() 用于计算形状的面积。 get_area() 内用pass占位

创建子类Circle和Rectangle，分别继承于Shape类，重写get_area()方法分别计算圆形和矩形的面积。

创建一个实例化的Circle和Rectangle对象，分别输出他们的颜色和面积。'''


'''class Yazi():  # 鸭子父类
    def __init__(self, typename, weight, height):
        self.type = typename
        self.weight = weight
        self.height = height


    def jiaosheng(self):
        print("嘎嘎")


    def info(self):
        print("种类:{},质量:{},身高:{}".format(self.type, self.weight, self.height))

class xiangpiya(Yazi):  # 橡皮鸭,Yazi是父类

    def __init__(self, typename, weight, height):
        super().__init__(typename, weight, height)

    def jiaosheng(self):  # 重写了Yazi父类的jiaosheng方法
        print("哈哈")

class Shuiya(Yazi):  # 水鸭,Yazi是父类
    def __init__(self, typename, weight, height):  # 继承了Yazi父类的jiaosheng方法
        super().__init__(typename, weight, height)

class Yeya(Yazi):  # 野鸭,Yazi是父类
    def __init__(self, typename, weight, height):
        super().__init__(typename, weight, height)

    def jiaosheng(self):  # 重写了 Yazi父类的jiaosheng方法
        print("咕咕")

xpy = xiangpiya("橡皮鸭", 3, 0.5)
xpy.info()
xpy.jiaosheng()

sy = Shuiya("水鸭", 5, 0.3)
sy.info()
sy.jiaosheng()

yy = Yeya("野鸭", 2.8, 0.6)
yy.info()
yy.jiaosheng()'''



'''days_of_year 方法的算法步骤是:
1.用月month_days列表记住平年里每一个月的总天数。

2.如果年份year是闰年,则把2月的总天数改为29。

3.对于月份month和日期date_in_month,利用month_days列表累加1月到(month一1)月的天数,再加上当月的天数date_in_month,累计和就是最终结果'''



'''# 定义各种"积木块"（类）
class SquareBlock:      # 方形积木
    def place(self):    # 放置方法
        print("▢ 放置一个方形积木")

class TriangleBlock:    # 三角形积木
    def place(self):    # 放置方法
        print("△ 放置一个三角形积木")

class RoundBlock:       # 圆形积木
    def place(self):    # 放置方法
        print("○ 放置一个圆形积木")

# 多态的体现：搭积木函数
def build_toy(block):
    """搭积木：不关心是什么形状，只要它能被放置"""
    block.place()  # 同样的调用，不同的结果


#
# # 创建各种积木
blocks = [SquareBlock(), TriangleBlock(), RoundBlock()]
for block in blocks:
    build_toy(block)'''


'''class yazi():
    def __init__(self,typename,tizhong,shengao):
        self.typename=typename
        self.tizhong=tizhong
        self.shengao=shengao

    def jiaoshen(self):
        print('嘎嘎')
    def info(self):
        print(f'{self.typename},{self.tizhong},{self.shengao}')
class xiangpiya(yazi):
    def __init__(self,typename,tizhong,shengao):
        super().__init__(typename,tizhong,shengao)
    def jiaoshen(self):
        print('哈哈')
class shuiya(yazi):
    def __init__ (self,typename,tizhong,shengao):
        super().__init__(typename,tizhong,shengao)
    def jiaoshen(self):
        print('呵呵')
class yeya(yazi):
    def __init__(self,typename,tizhong,shengao):
        super().__init__(typename,tizhong,shengao)
    def jiaoshen(self):
        print('额额')


x = xiangpiya('小黑',11,0.4)
x.info()
x.jiaoshen()
s=shuiya('小红',10,0.3)
s.info()
s.jiaoshen()
e=yeya('小绿',9,0.2)
e.info()
e.jiaoshen()
'''


'''定义父类：
创建一个名为 Animal的父类
在该类中定义一个 move()方法，输出"动物在移动"
创建子类：
创建三个子类：Dog、Bird和 Fish，它们都继承自 Animal类
在每个子类中重写​ move()方法，使其输出：
Dog类：输出"狗在奔跑"
Bird类：输出"鸟在飞翔"
Fish类：输出"鱼在游泳"
实现多态函数：
编写一个函数 animal_move(animal)，该函数可以接受任何 Animal类型的对象
在函数内部调用传入对象的 move()方法
测试多态：
创建 Dog、Bird和 Fish的实例对象
将这些对象分别传递给 animal_move()函数
观察并验证：虽然调用的是同一个函数，但不同对象会产生不同的输出结果'''

'''class Animal():
    def move(self):
        print('动物在移动')
class Bog(Animal):
    def move(self):
        print('小狗在奔跑')
class Bird(Animal):
    def move(self):
        print('小鸟在飞翔')
class Fish(Animal):
    def move(self):
        print('小鱼在游泳')

def animal_move(sc):
    sc.move()
a=[Bog(),Bird(),Fish()]
for i in a:
    animal_move(i)'''



















