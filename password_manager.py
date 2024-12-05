def view_pass():
    with open("password_lst.txt","r") as f:
        print("Your passwords are :")
        for line in f.readlines():
            print(line)

def add_pass():
    userid = input("enter username :")
    pwd = input("enter password : ")

    with open("password_lst.txt","a") as f:
        f. writelines(userid + " : " + pwd + "\n" )
        print()

mainpass = input("enter password to view your list of passwords :")
while mainpass == "rupanjali123":
    ans = int(input("Enter 1 to view password or enter 2 to add password or any other number to quit: "))
    
    if ans == 1:
        view_pass()

    elif ans == 2:
        add_pass()

    else:
        break        