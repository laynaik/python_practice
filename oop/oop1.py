


# class Dog():
#     #class attribute remains same for all 
#     species="junglee"
#     def __init__(self,name,breed):
#         self.breed = breed
#         self.name = name
#     #methods (functions acting on object )
#     #operation/ action the are function inside class 
#     #attributes dont have() while methods have this  
#     def bark(self,number):
#         print("bhau bahu my name is {} the number is {}".format(self.name,number)) 



# my_dog=Dog('vismay','stray')
# print(my_dog.name)
# my_dog.bark(100)

class Sample():
    def __init__(self,name,no):
        self.name=name
        self.number=no
my_sample = Sample('vismay',118)
print(my_sample.name)
print(my_sample.number)

