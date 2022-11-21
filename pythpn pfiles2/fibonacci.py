import sys

def fibonacci(n):
    a=1
    b=1
    counter=0
    while True:
        if counter>n:
            return
        yield a
        a,b=b,a+b
        counter+=1
        print(a,end=" ")

num=int(input("enter a number?"))
f=fibonacci(num)
while True:
    try:
        print(next(f),end=" ")
    except StopIteration:
        sys.exit()
