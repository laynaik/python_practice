


class Dog():
    #class attribute remains same for all 
    species="junglee"
    def __init__(self,name,breed):
        self.breed = breed
        self.name = name
    #methods (functions acting on object )
    #operation/ action the are function inside class 
    #attributes dont have() while methods have this  
    def bark(self,number):
        print("bhau bahu my name is {} the number is {}".format(self.name,number)) 



my_dog=Dog('vismay','stray')
print(my_dog.name)
my_dog.bark(100)

from cmath import pi


class Circle():
    pi=3.14

    def __init__(self,r):
        self.radius=r
    def circumference(self):
        c=self.radius*self.pi*2
        print(c)
mc=Circle(2)
print(mc.circumference)
