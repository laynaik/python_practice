#class inheritance
class Vehicle():
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage

    def seating_capacity(self,capacity):
        print("the seating capacity of {} is {}".format(self.name,capacity))
class Bus(Vehicle):
   
        
    def seating_capacity(self,capacity=50):
        return super().seating_capacity(50)
        
my_bus = Bus('bus',100,4)
print(my_bus.seating_capacity())
Bus.seating_capacity


