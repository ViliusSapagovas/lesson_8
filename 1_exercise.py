username_password_dict = {"first": "first12345", "second": "second23456", "third": "third34567", "fourth": "fourth45678", "fifth": "fifth56789"}

i=0
while i < 2:
    
    username = input("Enter username: ")
    for key in username_password_dict.keys():    
        if username == key:
            i += 1
            break
        
    if i == 0:
        print("This username doesn't excist, try again: ")
        continue

    password = input("Enter password: ")
 
    if password == username_password_dict[key]:
        i += 1
        print("Welcome :)")

    if i == 1: 
        print("Wrong password, try again: ")
        i=0