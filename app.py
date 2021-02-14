
import tkinter as tk
import string
import random
import os.path
from os import path
from datetime import date

today = date.today()
characters = string.printable[0:-6]
# Sep-16-2019
formated_date = today.strftime("%b-%d-%Y")


app = tk.Tk()
app.geometry("400x300")



selection = int(input("""

#######################
#                     #     
#        Menu         #
#                     #
#######################
1. Command Line App
2. Tkinter GUI App
3. close
Please Enter Your Choice:"""))

# generated_pass= ""

def passgencli():

    password_length = int(input("Please Enter Password Length:"))
    password = ""

    for i in range(password_length+1):
        password +=random.choice(characters)
    
    if (path.exists("Generated_Passwords.txt")):
        f = open("Generated_Passwords.txt", "a")
        f.write(formated_date + "\t \t \t \t \t" + password +"\n")
        f.close()
        print("saved to the password archive!")
    else:
        f = open("Generated_Passwords.txt", "w")
        f.write(formated_date + "\t \t \t \t \t" + password +"\n")
        f.close()
        print("saved to the password archive!")
    
    print("your generated password is: " + password)




# def passgengui():

#     password_length = int(input("Please Enter Password Length:"))
#     password = ""

#     for i in range(password_length+1):
#         password +=random.choice(characters)
#     generated_pass = password



if selection == 1:
    passgencli()


elif selection == 2:
    print("Under Development")
    # button = tk.Button(app,text="Generate Password",command = passgengui() )
    # button.grid(row=1, column=1)
    # label = tk.Label(app, font=("times", 15, "bold"))
    # label.config(text=generated_pass)
    # label.grid(row=4, column=2)
    # app.mainloop()
    
elif selection ==3:
    exit()
else:
    print("invalid Entry")




