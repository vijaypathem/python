list =[2,3,4,7,9]
target=12
x=0;y=1
n=len(list)
def add(x,y):
    for i  in range(n):  
        if list[x] + list[y]==target:
            print(f"indexes are {x} and {y}")
            return
        else:
            x+=1
            y+=1
add(x,y)