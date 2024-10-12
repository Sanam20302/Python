def check_pass(word):
    alph=Alph=num=char=False
    if (len(word)<6):
        print("It should contain atleast 6 letters")
        return False
    
    for i in word:
            if(i.isalpha() and i.islower()):
                alph = True
            if(i.isalpha() and i.isupper()):
                Alph = True
            if(i.isnumeric()):
                num=True
            if (i in "@#$%&"):
                char=True
    if (alph==Alph==num==char==True):
        return True
    return False

word = input("Enter the password :")
if (check_pass(word)):
     print("Valid")
else:
     print("Not valid")
