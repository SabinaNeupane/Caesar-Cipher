letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
msg=input("enter your string : ")
n_msg=""
for i in msg.upper():
    if i != " ":
        idx=letters.index(i)
        n_msg=n_msg+(letters[idx+3])
    else:
        n_msg=n_msg+" "
print(n_msg)