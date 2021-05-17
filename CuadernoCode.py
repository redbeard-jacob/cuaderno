from tkinter import *
from tkinter import filedialog
from tkinter import font
import time
import os
import sys

root = Tk()
root.title("Cuaderno - Untitled")
root.iconbitmap('C:/Users/Wall Brothers/Desktop/cuaderno/Cuaderno Code icon.ico')
root.geometry("1200x600")

global open_status_name
open_status_name = False
global selected
selected=False

#Create New File Function
def new_file():
    #delete previous text
    my_text.delete("1.0", END)
    #load new file
    root.title("Creating File")
    time.sleep(2)

    #Update status bars
    root.title("Cuaderno - NewFile")
    status_bar.config(text="Cuaderno - NewFile        ")
    global open_status_name
    open_status_name = False

#open files
def open_file():
    #delete previous text
    my_text.delete("1.0", END)
    
    #grab filename
    text_file = filedialog.askopenfilename(defaultextension="*.txt", initialdir="C:/Users/Wall Brothers/Desktop", title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))

    if text_file:
      root.title("Opening File...")

      time.sleep(3)
  
      #check if file opened
      if text_file:
      #make opened file global file
          global open_status_name
          open_status_name = text_file
    
      #update status bars
      name = text_file
      status_bar.config(text=f'{name}        ')
      name = name.replace("C:/Users/", "")
      root.title(f'{name} - Cuaderno')

      #open file
      text_file = open(text_file, 'r')
      stuff = text_file.read()
      #add file to textbox
      my_text.insert(END, stuff)
      #close the opened file
      text_file.close()

#Save as command
def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension="*.txt", initialdir="C:/Users/Wall Brothers/Desktop", title="Save File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    if text_file:

        #load saved file
        root.title("Saving File in Folder...")
        time.sleep(3)

        #update status bars
        name = text_file
        status_bar.config(text=f'{name}        ')
        name = name.replace("C:/Users/Wall Brothers/Desktop/", "")
        root.title(f'{name} - Cuaderno')

        #save the file
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))
        #close the file
        text_file.close()

#create save file function
def save_file():
    global open_status_name
    if open_status_name:
        root.title("Saving...")
        time.sleep(3)
        #save the file
        text_file = open(open_status_name, 'w')
        text_file.write(my_text.get(1.0, END))
        #close the file
        text_file.close()

        status_bar.config(text=f' Saved File: {open_status_name}        ')
        root.title(f' Saved File: {open_status_name} - Cuaderno')
    else:
        save_as_file()

#cut text, paste text and copy text
def cut_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if my_text.selection_get():
            #grab selected
            selected = my_text.selection_get()
            #delete selected
            my_text.delete("sel.first", "sel.last")
        root.clipboard_clear()
        root.clipboard_append(selected)
        status_bar.config(text=f"selected words: {selected}")
         
def copy_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    if my_text.selection_get():
        #grab selected
        selected = my_text.selection_get()
        root.clipboard_clear()
        root.clipboard_append(selected)
        
        status_bar.config(text=f"selected words: {selected}")

def paste_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:

        if selected:
            position = my_text.index(INSERT)
            my_text.insert(position, selected)
            
def run():
    import terminal

# create main frame
my_frame = Frame(root)
my_frame.pack(pady=5)

#create scrollbar for text box
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

#Horizontal ScrollBar
hor_scroll = Scrollbar(my_frame, orient='horizontal')
hor_scroll.pack(side=BOTTOM, fill=X, ipady=5)

#create text box
my_text = Text(my_frame, width=197, height=40, font=("Liberation Serif", 13), selectbackground="black", selectforeground="yellow", undo=True, yscrollcommand=text_scroll.set, wrap="none", xscrollcommand=hor_scroll.set)
my_text.pack()

#config scrollbar
text_scroll.config(command=my_text.yview)
hor_scroll.config(command=my_text.xview)

#create menu
my_menu = Menu(root)
root.config(menu=my_menu)

#add file menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="new", command=new_file)
file_menu.add_command(label="open", command=open_file)
file_menu.add_command(label="save", command=save_file)
file_menu.add_command(label="save as", command=save_as_file)
file_menu.add_command(label="run", command=run)
file_menu.add_separator()
file_menu.add_command(label="exit", command=root.destroy)

#add edit menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="cut        ", command=lambda:cut_text(False), accelerator="(Ctrl X)")
edit_menu.add_command(label="copy       ", command=lambda:copy_text(False), accelerator="(Ctrl C)")
edit_menu.add_command(label="paste      ", command=lambda:paste_text(False), accelerator="(Ctrl V)")
edit_menu.add_separator()
edit_menu.add_command(label="undo", command=my_text.edit_undo, accelerator="(Ctrl Z)")
edit_menu.add_command(label="redo", command=my_text.edit_redo, accelerator="(Ctrl Y)")

#add Status Bar
status_bar = Label(root, text="Cuaderno - Untitled", anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

#edit binding
root.bind('<Control-x>', cut_text)
root.bind('<Control-c>', copy_text)
root.bind('<Control-v>', paste_text)

fee = "Dogs"
my_label = Label(root, text=fee[:-1]).pack()

root.mainloop()
