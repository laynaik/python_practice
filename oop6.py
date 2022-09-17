#class inheritance 



class Vehicle():
    def __init__(self,name,max_speed,mileage,capacity):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
        self.capacity=capacity

    def fare(self):
        return self.capacity*100

class Bus(Vehicle):
    def fare(self):
       amt = super().fare()
       amt += amt*10/100
       return amt


volvo=Bus(250,10,2,50)

print(volvo.fare())
