from tkinter import *
import os
 
# Main window when user opens application 
def main():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x300")
    main_screen.title("Login Or Register")
    Label(text = "Select Your Choice", bg = "aqua", width = "300", height = "2", font =("Helvetica", 15)).pack()
    Label(text = "").pack()
    Button(text = "Login", height = "2", width = "30", command = login).pack()
    Label(text = "").pack()
    Button(text = "Register", height = "2", width = "30", command = register).pack()
    main_screen.mainloop()

# Register window
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x300")
    global username
    global password
    global enter_username
    global enter_password
    username = StringVar()
    password = StringVar()
    Label(register_screen, text="Please enter your details below:", bg="red").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ") # asterisk (*) means that field is required
    username_lable.pack()
    enter_username = Entry(register_screen, textvariable = username)
    enter_username.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    enter_password = Entry(register_screen, textvariable=password, show='*')
    enter_password.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="red", command = register_user).pack()
 
 
# Login window
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter your details below to login").pack()
    Label(login_screen, text="").pack()
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 
# What happens when user successfully or unsuccessfully registers
def register_user():
    username_info = username.get()
    password_info = password.get()
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
    enter_username.delete(0, END)
    enter_password.delete(0, END)
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 
# What happens when user successfully or unsuccessfully logs in
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    f.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
# Alert user when login is successful
def login_success():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
 
# Alert user when password is not recognised
def password_not_recognised():
    global password_not_recognised_screen
    password_not_recognised_screen = Toplevel(login_screen)
    password_not_recognised_screen.title("Success")
    password_not_recognised_screen.geometry("150x100")
    Label(password_not_recognised_screen, text="Invalid Password ").pack()
    Button(password_not_recognised_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Delete the alerts
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recognised_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
if __name__ == "__main__":
    main()