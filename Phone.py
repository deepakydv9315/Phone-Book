import tkinter as tk
from tkinter import ttk
deep = tk.Tk()
deep.title("Phone")

name_var = tk.StringVar()
group_var = tk.StringVar()
phone_var = tk.IntVar()

def out() :
    exit()

def action():
    user_name = name_var.get()
    user_group = group_var.get()
    user_phone = phone_var.get()
    print(f"Name ---> {user_name}")
    print(f"Group ---> {user_group}")
    print(f"Ph. no. ---> {user_phone}")

    with open('Phone.txt' , 'a') as f:
        f.write(f">>> Name:- {user_name}   Phone No.:- {user_phone}   Group:- {user_group}\n\n")
       
         
    name_entrybox.delete(0 , tk.END)  
    phone_entrybox.delete(0 , tk.END)       

def clean():
    name_entrybox.delete(0 , tk.END)  
    phone_entrybox.delete(0 , tk.END)  

heading_label = ttk.Label(deep , text = 'PHONE BOOK').grid(row = 0 , column = 1)
name_label = ttk.Label(deep , text = 'Enter Name :-   ' )
name_label.grid(row = 1, column = 0 , sticky = tk.W)
name_entrybox = ttk.Entry(deep , width = 13 , textvariable = name_var)
name_entrybox.grid(row = 1 , column = 1)
name_entrybox.focus()

phone_label = ttk.Label(deep , text = 'Ph. Number:-')
phone_label.grid(row = 2, column = 0 , sticky = tk.W)
phone_entrybox = ttk.Entry(deep, width = 13 , textvariable = phone_var )
phone_entrybox.grid(row = 2 , column= 1 )

group_label = ttk.Label(deep , text = 'Group')
group_label.grid(row=3 , column = 0 , sticky = tk.W)
group_combo = ttk.Combobox(deep , width = 10 , state = 'readonly' , textvariable = group_var )
group_combo.grid(row=3 , column = 1 )
group_combo['values'] = ('Friend' , 'Family' , 'Work' , 'School')
# group_combo.current(0)

submit_button = ttk.Button(deep , text = 'Submit',command = action).grid(row=4 , column=1)
exit_button = ttk.Button(deep, text = 'Exit',command = out).grid(row =4 ,column=2)
clear_button = ttk.Button(deep , text= 'Clear' , command = clean).grid(row = 4 , column = 0)

deep.mainloop()



