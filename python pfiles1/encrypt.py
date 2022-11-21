alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encrypt(text,shift_num,direction):
    new_text=""
    if(direction=="decode"):
        shift_num*=-1
    for element in text:
        if element in alphabet:
            position=alphabet.index(element)
            new_position=position+shift_num
            letter=alphabet[new_position]
            new_text+=letter
        else:
            new_text+=element
    print(f"your {direction}ed text is : {new_text}")
shoud_continue=True
while shoud_continue:
  text=input("Enter your text\n")
  shift_num=int(input("enter shift number\n"))
  shift_num%=26
  direction=input("encode||decode\n")
  encrypt(text,shift_num,direction)
  result=input("do you want to continue: yes or no\n")
  if(result=="no"):
    shoud_continue=False
    print("goodbye")
