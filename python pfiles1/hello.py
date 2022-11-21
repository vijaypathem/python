
from asyncore import write


name=input("whats your name")

file=open("names.txt","a")
file.write(f"{name} \n")
file.close()