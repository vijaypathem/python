class Car:

    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer=20

    def about_car(self):
        data=f"{self.make} {self.model} {self.year}"
        return data.title()
    def reading(self):
        print(f"{self.odometer} miles on it")
    def update_reading(self,miles):
        if miles>=self.odometer:
            self.odometer=miles
        else:
            print("you cant roll back reading")
    def incr_reading(self,miles):
        self.odometer+=miles

class Electric_car(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Battery()
    
class Battery():
    def __init__(self,capacity=100):
        self.capacity=capacity

    def battery_capacity(self):
        print(f"this car has {self.capacity} kwh battery")



e_car=Electric_car("tesla","model s","2020")
print(e_car.about_car())
e_car.reading()
e_car.battery.battery_capacity()
e_car.update_reading(45)
e_car.reading()
e_car.incr_reading(10)
e_car.reading()