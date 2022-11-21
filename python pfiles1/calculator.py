def add(n1,n2):
    return n1+n2
def mul(n1,n2):
    return n1*n2
def sub(n1,n2):
    return n1-n2
def div(n1,n2):
    return n1/n2
operators={
    "+":add,
    "*":mul,
    "-":sub,
    "/":div
}
print("welcome")
def calc():
    first_num=float(input("enter number"))
    should_continue=True
    while should_continue:
        for symbol in operators:
            print(symbol)
        op=input("select an operator")
        next_num=float(input("enter next number"))
        calculation=operators[op]
        answer=calculation(first_num,next_num)
        print(f"{first_num} {op} {next_num} = {answer}")
        if(input("do you want to continue y||n")=="y"):
            first_num=answer
        else:
            calc()

calc()
    