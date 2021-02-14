# Importing Tkinter for GUI Interface
import tkinter as tk

#importing String for ASCII characters
import string

#Importing Random library to generate and choose random characters to create passwords
import random

# Os library to check paths i.e. if the file exist or not
import os.path
from os import path

# Importing datetime module to cater todays date
from datetime import date

# initializing date Module for current date
today = date.today()

# Removing extra variables like white space, tabs and other form of format specifiers
characters = string.printable[0:-6]

# formating date like thi Sep-16-2019
formated_date = today.strftime("%b-%d-%Y")

# Initializing tkinter app
app = tk.Tk()

# seeting up geometry for app i.e. windows size
app.geometry("400x300")


# Long string for menu printing
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

generated_pass= ""

def passgencli():

    password_length = int(input("Please Enter Password Length:"))
    password = ""

    # looping over the length and choosing random characters to generate a password
    for i in range(password_length+1):
        password +=random.choice(characters)
    
    # Checking if the file exist or not, if it doesn't then create a new one otherwise append the existing one
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




def passgengui():

    password_length = int(input("Please Enter Password Length:"))
    password = ""

    for i in range(password_length+1):
        password +=random.choice(characters)
    generated_pass = password



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




