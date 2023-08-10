from category import category
import tkinter as tk
from tkinter import ttk
import time

import pickle as pk
import os




category_list = []

for item in os.listdir() :  #loading the saved objects
    if item[-4::1] == ".pkl" :
        with open(item , "rb") as file :
            category_list.append(pk.load(file))

window = tk.Tk()

window.geometry("600x400" )
notebook = ttk.Notebook(window)
notebook.pack()
objectives = tk.Frame(notebook ,width=600 , height=400 , bg= "#ebbfd0")
objectives.pack()
notebook.add(objectives, text="objectives")
category_text_label = tk.Label(objectives , text="category:" , bg = "#ebbfd0" , font="MathJax_TypeWriter") 
category_text_label.place( x=0 , y= 30)
list1 = [item.name for i in category_list] #cat list
window.configure(bg= "#ebbfd0")

list_box = tk.Listbox(objectives , bg= "#e9d9db") 
def delete():
    global list_box

    selection=list_box.curselection()
    picked = list_box.get(selection[0])
    for items in category_list:
        if items.name == category_list_combobox.get():
            items.data.pop(items.data.index(picked))
    list_refresh()
    


list_box.place(x=32,y=110)
delete_button = tk.Button(objectives , command= delete , text= "Delete" , bg="#f57cab" , font="MathJax_TypeWriter")
delete_button.place(x = 314, y = 180)
list_box.place(x = 150 , y = 140)

def list_refresh():
    global list_box 
    list_box = tk.Listbox(objectives,bg= "#e9d9db") 
    for item in category_list :
        if item.name == category_list_combobox.get():
            for x in item.data:
                list_box.insert(0,x)
    list_box.place(x = 150 , y = 140)
    
refresh_button = tk.Button(objectives, text= "refresh" , command=list_refresh , bg = "#f57cab" , font="MathJax_TypeWriter")
refresh_button.place(x= 314, y=140)

item_label = tk.Label(objectives , text= " item:" , bg = "#ebbfd0" , font="MathJax_TypeWriter")
item_label.place(x=0 , y = 90)

entry = tk.Entry(objectives ,width = 15 , bg="#e9d9db" , font="MathJax_TypeWriter")
entry.place( x = 80, y = 90)




category_list_combobox = ttk.Combobox(objectives ,values= list1  ,postcommand=list_refresh  )
style = ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground= "#e9d9db", background= "#e9d9db")

category_list_combobox.place(x=80 , y = 30)


def add_cat():
    global category_list_combobox
    global list1

    item = category_list_combobox.get()
    category_list.append(category(item , "red"))
    list1 = [i.name for i in category_list]
    category_list_combobox = ttk.Combobox(objectives ,values= list1 )
    category_list_combobox.place(x=80 , y = 30)
    list_refresh()

add_cat_button = tk.Button(objectives , text= "Add" , command=add_cat , bg="#f57cab" , font="MathJax_TypeWriter")
add_cat_button.place(x = 280 , y = 30)
def add():
    item = category_list_combobox.get()
    index = list1.index(item)
    category_list[index].data.append(entry.get())
    print(category_list[index].data)
    list_refresh()
    
add_button = tk.Button(objectives , text= "Add" , command=add , bg="#f57cab" , font="MathJax_TypeWriter") 
add_button.place(x= 220 , y =90)

#--------====================== timer tab ===========-----------------


timer_tab = tk.Frame(notebook , width= 600 , height= 400  ,bg="#ebbfd0")
timer_tab.pack()
notebook.add(timer_tab , text="timer"   )


seconds = 0 
mins = 0
hours = 0

start_stop = False

Timer_label = tk.Label( timer_tab, text= f"{hours:02}:{mins:02}:{seconds:02}", bg="#f57cab" , font="MathJax_TypeWriter" )
Timer_label.config(font=("MathJax_TypeWriter" , 50))
Timer_label.place(x = 160 , y = 160)
def start_timer():
    global Timer_label
    global start_stop
    global seconds
    global mins
    global hours


    
    
    if start_stop == True : 
        Timer_label.after(1000 , start_timer)
    
    seconds +=1
    if seconds == 60 :
        seconds =0
        mins +=1
    if mins == 60 :
        mins = 0 
        hours +=1 
    Timer_label = tk.Label( timer_tab, text= f"{hours:02}:{mins:02}:{seconds:02}", bg="#f57cab" , font="MathJax_TypeWriter" )
    Timer_label.place(x = 160 , y = 160)
    Timer_label.config(font=("MathJax_TypeWriter" , 50))
def start():
    
    global start_stop
    if start_stop == False :
        start_stop = True 
        start_timer()

def stop():
    global start_stop
    if start_stop == True :
        start_stop = False
start_button = tk.Button(timer_tab , text="start" , command= start ,bg="#f57cab" , font="MathJax_TypeWriter" )
start_button.place(x =160 , y = 230)
stop_button = tk.Button(timer_tab , text= "stop" , command= stop, bg="#f57cab" , font="MathJax_TypeWriter" )
stop_button.place(x =384 , y = 230)
tk.Label(timer_tab , text= "category:" ,bg="#ebbfd0" , font="MathJax_TypeWriter" ).place(x = 120 , y = 100)
def combo_refresh():
    global cat_combo
    global list1
    cat_combo = ttk.Combobox(timer_tab  , value = list1  )
    cat_combo.place(x= 200 , y = 100)
cat_combo = ttk.Combobox(timer_tab  , value = list1   )
cat_combo.place(x= 200 , y = 100)
reftresh_cat_button = tk.Button(timer_tab , text = "refresh" , command= combo_refresh , bg="#f57cab" , font="MathJax_TypeWriter")
reftresh_cat_button.place(x= 390 , y = 100)
window.mainloop()