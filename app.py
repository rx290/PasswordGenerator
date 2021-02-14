

import random
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*()_+-=~`[}]{\;'./1234567890?><"




selection = int(input("""

#######################
#                     #     
#        Menu         #
#                     #
#######################
1. Command Line App
2. Tkinter GUI App
Please Enter Your Choice:"""))

if selection == 1:
    password_length = int(input("Please Enter Password Length:"))
    password = ""

    for i in range(password_length+1):
        password +=random.choice(characters)
    print("your generated password is: " + password)