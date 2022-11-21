class Restaurant:
    def __init__(self,name,special):
        self.name=name
        self.special=special
    def open(self):
        print(f"{self.name} restaurant is open now")
    def about(self):
        print(f"{self.name} has a special item {self.special}")

restaurant1=Restaurant("mehfil","biryani")
restaurant2=Restaurant("kritunga","chicken mandi")
restaurant3=Restaurant("dominos","pizza")
restaurant1.open()
restaurant1.about()
print()
restaurant2.open()
restaurant2.about()
print()
restaurant3.open()
restaurant3.about()
