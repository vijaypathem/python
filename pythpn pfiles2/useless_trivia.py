name=input("what is your name?")
age=input("what is your age?")
weight=int(input("last question!,how many kg's do you weigh?"))

print(f"you are receiving a mail, the boy calls you: {name}\n your details on adhar are printed as:\n name:{name}\n age:{age}")
#weight on moon
def w_moon(n):
    return(n*1.6).round()
print(f"your weight on the moon is: {w_moon(weight)}")