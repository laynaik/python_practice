#excersise 3 child class bus that will inhert all the variables and methods of vehicle class
class Vehicle():
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
class Bus(Vehicle):
    pass