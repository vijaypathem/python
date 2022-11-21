print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
comb=name1+name2
t1=0
t2=0
comb.lower()
t=comb.count("t")
r=comb.count("r")
u=comb.count("u")
e=comb.count("e")
t1=t+r+u+e
a=str(t1)
l=comb.count("l")
o=comb.count("o")
v=comb.count("v")
e=comb.count("e")
t2=l+o+v+e
b=str(t2)
z=int(a+b)
print("your love percentage is:",z)
c=int(z)
if z<40:
  print("buddy this is just for fun")
else:
  print("happy life, fight for ur love buddy")
