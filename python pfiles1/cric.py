def t20(cu_overs,c_sc,target):
    re_over=20-cu_overs
    re_sc=target-c_sc
    return re_sc/re_over

def test(cu_overs,c_sc,target):
    re_over=90-cu_overs
    re_sc=target-c_sc
    return re_sc/re_over

def oneday(cu_overs,c_sc,target):
    re_over=50-cu_overs
    re_sc=target-c_sc
    return re_sc/re_over

game=int(input("select tournament:\n 1. T20 \n 2. OneDay \n 3. Test\n"))

cu_overs=int(input("enter current over:\n"))
c_sc=int(input("enter current score:\n"))
target=int(input("enter target:\n"))
if game==1:
    run_rate =t20(cu_overs,c_sc,target)
    print(f"your required runrate is: {run_rate}")
elif game==2:
    run_rate =oneday(cu_overs,c_sc,target)
    print(f"your required runrate is: {run_rate}")
else:
    run_rate =test(cu_overs,c_sc,target)
    print(f"your required runrate is: {run_rate}")
