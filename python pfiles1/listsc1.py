list =(10,20,-2,9,-8,4,3,-7,23,8,-6,-11)
positive=0
negative=0
for i in range(len(list)):
 if(list(i)>0):
    positive=positive+1
 else:
    negative=negative+1
print(f"the positive numers are:{positive}")
print(f"the negative numers are:{negative}")
nextlist=()
for k in range(len(list)):
    if(k%2==1):
        if(list(k)>0):
            nextlist+=(k)
    else:
        if(list(k)<0):
            nextlist+=(k)
print(nextlist)