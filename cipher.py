letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
while True:
    n_msg=""
    print("Welcome to Caesar Cipher")
    print('''Pick from the following options : 
    1. Encrypt
    2. Exit ''')
    opt=int(input("enter your choice : "))
    def input_shell(msg):
                for i in msg.upper():
                    global n_msg
                    if i != " ":
                        idx=letters.index(i)
                        n_msg=n_msg+(letters[idx+3])
                    else:
                        n_msg=n_msg+" "
                return n_msg        
    if opt==1:
        ec=input_shell(input("enter your string : "))
        print()
        print(f"the message is {ec}")
        print()
    if opt==2:
        print("you have exited the program")
        break

