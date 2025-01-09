import tkinter as tk
from PIL import ImageTk, Image
import subprocess
from tkinter.messagebox import showerror
import ast


#GUI
root=tk.Tk()
root.title('Login')
root.geometry('1024x640')
root.resizable(False,False)
root.config(bg='white')

#Def Function
def create():
    root.destroy()
    subprocess.run(['python','Buat Akun.py'])

def delete():
    root.destroy()
    subprocess.run(['python','Hapus Akun.py'])


#Frame 1 left
frame1_left=tk.Frame(root,pady='3cm',bg='white')
frame1_left.grid()

Image1=Image.open('Foto\login.jpg')
Image_main=ImageTk.PhotoImage(Image1)
main_image=tk.Label(frame1_left,image=Image_main,border=0,bg='white')
main_image.grid(row=0,column=0,padx=100)

#Frame 1 right
frame1_right=tk.Frame(root,borderwidth=1,bg='white')
frame1_right.grid(row=0,column=1)

heading=tk.Label(frame1_right, text='Selamat Datang',fg='#BE6557',bg='white',font=('Roboto',23))
heading.grid(row=0,column=0,pady=20)

#Def Username
def on_enter(a):
    user_ent.delete(0,'end')
   
def on_leave(a):
    if user_ent.get()=='':
        user_ent.insert(0,'Username')
        

user_ent=tk.Entry(frame1_right,fg='black',bg='white',border=0,font=('Roboto',11),width=27)
user_ent.grid(row=1,column=0)
user_ent.insert(0,'Username')
user_ent.bind('<FocusIn>',on_enter)
user_ent.bind('<FocusOut>',on_leave)
tk.Frame(frame1_right,width=230,height=2,bg='black').grid()

space=tk.Label(frame1_right,border=0,bg='white')
space.grid(row=3,column=0,pady=10)

#Def Password
def on_enter(a):
    pass_ent.delete(0,'end')
    pass_ent.config(fg='black', show='*')
def on_leave(a):
    if pass_ent.get()=='':
        pass_ent.insert(0,'Password')
        pass_ent.config(fg='black', show='')

pass_ent=tk.Entry(frame1_right,fg='black',bg='white',border=0,font=('Roboto',11),width=27)
pass_ent.grid(row=4,column=0)
pass_ent.insert(0,'Password')
pass_ent.bind('<FocusIn>',on_enter)
pass_ent.bind('<FocusOut>',on_leave)
tk.Frame(frame1_right,width=230,height=2,bg='black').grid()


def mas():
    username=user_ent.get()
    password=pass_ent.get()
    
    file=open('Data\pw.txt','r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()

    if username in r.keys() and password==r[username]:
        root.destroy()
        subprocess.run(['python','Home.py'])
    
    else:
        showerror('Invalid','invalid')

    

login=tk.Button(frame1_right,bg='#BE6557',width=17,border=0,text='Masuk',fg='white',font=('Roboto',17),command=mas)
login.grid(row=6,column=0,pady=10)

crate_ac=tk.Label(frame1_right,bg='white',fg='black',text='Belum punya akun?',border=0)
crate_ac.grid(row=7,column=0)

crate_act=tk.Button(frame1_right,bg='white',fg='blue',text='Buat Akun',border=0,command=create)
crate_act.grid()

delete_act=tk.Button(frame1_right,bg='white',fg='blue',text='Hapus Akun',border=0,command=delete)
delete_act.grid()


root.mainloop()