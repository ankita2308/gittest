class DemoClass:
    name='python'
    def __init__(self,a,b):
        print('this is demo class')
        self.a=a
        self.b=b
    def display(self):
        print(self.a,self.b)
obj=DemoClass(10,20)
obj.display()
print(obj.name)
print(DemoClass.name)
print(obj.a,obj.b)
print(DemoClass.a)


L=[1,2,3]
L=L+"python"
print(L)
