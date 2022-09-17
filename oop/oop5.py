#propert that has same value for every class instance 
class Vehicle():
    fuel = 'petrol' #class object attribute 
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
class Bus(Vehicle):
    pass
class Car(Vehicle):
    pass
volvo=Bus("bacardi",100,2)
print("the name of bus is {} and fuel type is {}".format(volvo.name,volvo.fuel))
