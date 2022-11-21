class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        print(f"{self.name} sat on the bench")

    def roll_ovr(self):
        print(f"{self.name} rolled over")

my_dog=Dog("willie",4)
print(f"my dog name is {my_dog.name}")
print(f"{my_dog.name} is {my_dog.age} years old")
my_dog.sit()
my_dog.roll_ovr()
print("*"*20,end="",)
print()
other_dog=Dog("billie",3)
print(f"other dog name is {other_dog.name}")
print(f"{other_dog.name} is {other_dog.age} years old")
other_dog.sit()
other_dog.roll_ovr()