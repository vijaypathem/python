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


car1=Car("swift","dezire",2020)
car2=Car("tata","nexon",2017)
car3=Car("kia","centuro",2018)
car4=Car("tata","indica",2014)
print(car1.about_car())
car1.reading()
print(car2.about_car())
car2.odometer=10
car2.reading()
print(car3.about_car())
car3.update_reading(55)
car3.reading()
print(car4.about_car())
car4.incr_reading(20)
car4.reading()