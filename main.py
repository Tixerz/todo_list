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

window.geometry("600x400" )

category_text_label = tk.Label(text="category:" , bg = "#ebbfd0" , font="MathJax_TypeWriter") 
category_text_label.place( x=0 , y= 10)
list1 = [item.name for i in category_list] #cat list
window.configure(bg= "#ebbfd0")

list_box = tk.Listbox(window , bg= "#e9d9db") 
def delete():
    global list_box

    selection=list_box.curselection()
    picked = list_box.get(selection[0])
    for items in category_list:
        if items.name == category_list_combobox.get():
            items.data.pop(items.data.index(picked))
    list_refresh()
    


list_box.place(x=32,y=90)
delete_button = tk.Button(window , command= delete , text= "Delete" , bg="#f57cab" , font="MathJax_TypeWriter")
delete_button.place(x = 314, y = 160)
list_box.place(x = 150 , y = 120)

def list_refresh():
    global list_box 
    list_box = tk.Listbox(window,bg= "#e9d9db") 
    for item in category_list :
        if item.name == category_list_combobox.get():
            for x in item.data:
                list_box.insert(0,x)
    list_box.place(x = 150 , y = 120)
    
refresh_button = tk.Button(window , text= "refresh" , command=list_refresh , bg = "#f57cab" , font="MathJax_TypeWriter")
refresh_button.place(x= 314, y=120)

item_label = tk.Label(window , text= " item:" , bg = "#ebbfd0" , font="MathJax_TypeWriter")
item_label.place(x=0 , y = 70)

entry = tk.Entry(window ,width = 15 , bg="#e9d9db" , font="MathJax_TypeWriter")
entry.place( x = 80, y = 70)




category_list_combobox = ttk.Combobox(window ,values= list1  ,postcommand=list_refresh  )
style = ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground= "#e9d9db", background= "#e9d9db")

category_list_combobox.place(x=80 , y = 10)


def add_cat():
    global category_list_combobox
    global list1

    item = category_list_combobox.get()
    category_list.append(category(item , "red"))
    list1 = [i.name for i in category_list]
    category_list_combobox = ttk.Combobox(window ,values= list1 )
    category_list_combobox.place(x=80 , y = 10)
    list_refresh()

add_cat_button = tk.Button(window , text= "Add" , command=add_cat , bg="#f57cab" , font="MathJax_TypeWriter")
add_cat_button.place(x = 280 , y = 10)
def add():
    item = category_list_combobox.get()
    index = list1.index(item)
    category_list[index].data.append(entry.get())
    print(category_list[index].data)
    list_refresh()
    
add_button = tk.Button(window , text= "Add" , command=add , bg="#f57cab" , font="MathJax_TypeWriter") 
add_button.place(x= 220 , y =70)

tk.Label(window , text = "====================================================================================").place(x=-2 , y=40)








window.mainloop()