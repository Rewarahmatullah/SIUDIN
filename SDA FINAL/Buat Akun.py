import tkinter as tk
from PIL import ImageTk, Image
import subprocess
import ast
from tkinter.messagebox import showinfo, showerror

window = tk.Tk()
window.title('Create')
window.geometry('1024x640')
window.resizable(False, False)
window.config(bg='white')


frame1_left = tk.Frame(window, pady='3cm', bg='white')
frame1_left.grid()

Image1 = Image.open('Foto/Buatakun.jpg')  # Ensure the path uses the correct separator
Image_main = ImageTk.PhotoImage(Image1)
main_image = tk.Label(frame1_left, image=Image_main, border=0, bg='white')
main_image.grid(row=0, column=0, padx=100)

frame1_right = tk.Frame(window, borderwidth=1, bg='white')
frame1_right.grid(row=0, column=1)

heading = tk.Label(frame1_right, text='Buat Akun', fg='#BE6557', bg='white', font=('Roboto', 23))
heading.grid(row=0, column=0, pady=10)

# --- Username
def on_enter(e):
    if user_ent.get() == 'Username':
        user_ent.delete(0, 'end')
        user_ent.config(fg='black')

def on_leave(e):
    if user_ent.get() == '':
        user_ent.insert(0, 'Username')
        user_ent.config(fg='black')

user_ent = tk.Entry(frame1_right, fg='black', bg='white', border=0, font=('Roboto', 11), width=27)
user_ent.grid(row=1, column=0)
user_ent.insert(0, 'Username')
user_ent.bind('<FocusIn>', on_enter)
user_ent.bind('<FocusOut>', on_leave)
tk.Frame(frame1_right, width=230, height=2, bg='black').grid()

space = tk.Label(frame1_right, border=0, bg='white')
space.grid(row=3, column=0, pady=5)

# --- Password
def on_enter(e):
    if pass_ent.get() == 'Password':
        pass_ent.delete(0, 'end')
        pass_ent.config(fg='black', show='*')

def on_leave(e):
    if pass_ent.get() == '':
        pass_ent.insert(0, 'Password')
        pass_ent.config(fg='black', show='')

pass_ent = tk.Entry(frame1_right, fg='black', bg='white', border=0, font=('Roboto', 11), width=27)
pass_ent.grid(row=4, column=0)
pass_ent.insert(0, 'Password')
pass_ent.bind('<FocusIn>', on_enter)
pass_ent.bind('<FocusOut>', on_leave)
tk.Frame(frame1_right, width=230, height=2, bg='black').grid()

space = tk.Label(frame1_right, border=0, bg='white')
space.grid(row=6, column=0, pady=5)

# --- Confirm
def on_enter(e):
    if passcon_ent.get() == 'Confirm Password':
        passcon_ent.delete(0, 'end')
        passcon_ent.config(fg='black', show='*')

def on_leave(e):
    if passcon_ent.get() == '':
        passcon_ent.insert(0, 'Confirm Password')
        passcon_ent.config(fg='black', show='')

passcon_ent = tk.Entry(frame1_right, fg='black', bg='white', border=0, font=('Roboto', 11), width=27)
passcon_ent.grid(row=7, column=0)
passcon_ent.insert(0, 'Confirm Password')
passcon_ent.bind('<FocusIn>', on_enter)
passcon_ent.bind('<FocusOut>', on_leave)
tk.Frame(frame1_right, width=230, height=2, bg='black').grid()

# --- Submit
def sub():
    username = user_ent.get()
    password = pass_ent.get()
    confirm = passcon_ent.get()

    if password == confirm:
        try:
            with open('Data\pw.txt', 'r+') as file:
                d = file.read()
                try:
                    r = ast.literal_eval(d)
                except:
                    r = {}
                dict2 = {username: password}
                r.update(dict2)
                file.seek(0)
                file.truncate()
                file.write(str(r))
            showinfo('Success', 'Account created successfully')
            window.destroy()
        except Exception as e:
            showerror('Error', str(e))
    else:
        showerror('Invalid', 'Password tidak sama')

submit = tk.Button(frame1_right, text='Submit', fg='white', border=0, bg='#BE6557', width=20, font=('Roboto', 14), command=sub)
submit.grid(row=9, column=0, pady=10)

window.mainloop()