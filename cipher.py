letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
while True:
    n_msg=""
    print("Welcome to Caesar Cipher")
    print('''Pick from the following options : 
    1. Encrypt
    2. Exit ''')
    opt=int(input("enter your choice : "))
    def input_shell(msg,sv):
                for i in msg.upper():
                    global n_msg
                    if i != " ":
                        idx=letters.index(i)
                        if (idx+sv)>(len(letters)-1):
                            o1=letters.index("Z")-idx
                            o2=sv-o1
                            n_msg=n_msg+(letters[o2-1])
                        else:
                             n_msg=n_msg+(letters[idx+sv])
                    else:
                        n_msg=n_msg+" "
                return n_msg        
    if opt==1:
        ec=input_shell(input("enter your string : "),int(input("enter your shift value : ")))
        print()
        print(f"the message is {ec}")
        print()
    if opt==2:
        print("you have exited the program")
        break

