class Cutecat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
            print(f'{self.name},是坐下')

    def gun(self):
            print(f'{self.age},成年')

if __name__=='__main__':
    cat1=Cutecat('小明',2)
    cat1.sit()
    cat1.gun()

