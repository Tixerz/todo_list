from category import category
import tkinter as tk
from tkinter import ttk
import pickle as pk
import os

category_list = []

for item in os.listdir() :  #loading the saved objects
    if item[-4::1] == ".pkl" :
        with open(item , "rb") as file :
            category_list.append(pk.load(file))

window = tk.Tk()
window.geometry("600x400")
category_text_label = tk.Label(text="category:")
category_text_label.place( x=0 , y= 10)
list1 = [item.name for i in category_list]


list_box = tk.Listbox(window) 
list_box.place(x = 0 , y = 80) 
def list_refresh():
    global list_box 
    list_box = tk.Listbox(window) 
    for item in category_list :
        if item.name == category_list_combobox.get():
            for x in item.data:
                list_box.insert(0,x)
    list_box.place(x = 0 , y = 80)
refresh_button = tk.Button(window , text= "refresh" , command=list_refresh)
refresh_button.place(x= 170, y=80)
item_label = tk.Label(window , text= " item:")
item_label.place(x=0 , y = 40)

entry = tk.Entry(window ,width = 15 )
entry.place( x = 80, y = 40)




category_list_combobox = ttk.Combobox(window ,values= list1 )
category_list_combobox.place(x=80 , y = 10)

def add_cat():
    global category_list_combobox
    global list1
    item = category_list_combobox.get()
    category_list.append(category(item , "red"))
    list1 = [i.name for i in category_list]
    category_list_combobox = ttk.Combobox(window ,values= list1 )
    category_list_combobox.place(x=80 , y = 10)

add_cat_button = tk.Button(window , text= "add" , command=add_cat)
add_cat_button.place(x = 280 , y = 10)
def add():
    item = category_list_combobox.get()
    index = list1.index(item)
    category_list[index].data.append(entry.get())
    print(category_list[index].data)
    
add_button = tk.Button(window , text= "add" , command=add)
add_button.place(x= 210 , y =40)

window.mainloop()