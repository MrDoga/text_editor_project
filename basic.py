from Tkinter import *
import Tkinter as tk
import ScrolledText
import tkFileDialog
import tkMessageBox
root = tk.Tk(className="Text Editor")
tp = ScrolledText.ScrolledText(root,width=150,height=100)

#functions

def dummy():
    tkMessageBox.showinfo("Dummy","No Function is added yet")

def new():
   root.title("Untitled")
   global file
   file = None
   tp.delete(1.0,END)


def open():
   file = tkFileDialog.askopenfile(parent=root, mode='rb', title='Select a file')
   if file != None:
      contents = file.read()
      tp.insert('1.0', contents)
      file.close()


def save(self):
   file = tkFileDialog.asksaveasfile(mode='w')
   if file != None:
      # slice off the last character from get, as an extra return is added
      data = self.textPad.get('1.0', END + '-1c')
      file.write(data)
      file.close()


def exit():
   if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
      root.destroy()


def about():
   label = tkMessageBox.showinfo("About", "Just Another TextPad \n Copyright \n No rights left to reserve")

def cut():
   tp.event_generate("<<Cut>>")
   return "break"

def copy():
   tp.event_generate("<<Copy>>")
   return "break"

def paste_file():
   tp.event_generate("<<Paste>>")
   return "break"

def undo_last():
   tp.event_generate("<<Undo>>")
   return "break"


##menubar###
# Insert a menu bar on the main window
menu = Menu(root)
root.config(menu=menu)

#submenu
submenu = Menu(menu)
menu.add_cascade(label='File',menu=submenu)
submenu.add_cascade(label='New',command=new)
submenu.add_separator()
submenu.add_cascade(label='Open',command=open)
submenu.add_cascade(label='Save',command=save)
submenu.add_separator()
submenu.add_cascade(label='Save As',command=dummy)
submenu.add_cascade(label='Exit',command=exit)


editmenu = Menu(menu)
menu.add_cascade(label='Edit',menu=editmenu)
editmenu.add_cascade(label='Undo',command=dummy)
submenu.add_separator()
editmenu.add_cascade(label='Redo',command=dummy)
editmenu.add_cascade(label='Cut',command=cut)
submenu.add_separator()
editmenu.add_cascade(label='Copy',command=copy)
editmenu.add_cascade(label='Paste',command=paste_file)

viewmenu = Menu(menu)
menu.add_cascade(label='View',menu=viewmenu)
viewmenu.add_cascade(label='Show NumberLine',command=dummy)

aboutmenu = Menu(menu)
menu.add_cascade(label="About",menu=aboutmenu)
aboutmenu.add_command(label="About...", command=about)
###ToolBar###
toolbar = Frame(root,bg="grey")#insert tool bar
new = PhotoImage(file="new.gif")
b1 = Button(toolbar,image=new,command=dummy)
b1.pack(side=LEFT,padx=2,pady=2)
open = PhotoImage(file="open.gif")
b2 = Button(toolbar,image=open,command=open)
b2.pack(side=LEFT,padx=2,pady=2)
save = PhotoImage(file="save.gif")
b3= Button(toolbar,image=save,command=save)
b3.pack(side=LEFT,padx=2,pady=2)
undo = PhotoImage(file="undo.gif")
b4= Button(toolbar,image=undo,command=dummy)
b4.pack(side=LEFT,padx=2,pady=2)
redo = PhotoImage(file="redo.gif")
b5= Button(toolbar,image=redo,command=dummy)
b5.pack(side=LEFT,padx=2,pady=2)
search = PhotoImage(file="search.gif")
b6= Button(toolbar,image=search,command=dummy)
b6.pack(side=LEFT,padx=2,pady=2)
cut = PhotoImage(file="cut.gif")
b7= Button(toolbar,image=cut,command=cut)
b7.pack(side=LEFT,padx=2,pady=2)
copy = PhotoImage(file="copy.gif")
b8= Button(toolbar,image=copy,command=copy)
b8.pack(side=LEFT,padx=2,pady=2)
paste = PhotoImage(file="paste.gif")
b9= Button(toolbar,image=paste,command=paste_file)
b9.pack(side=LEFT,padx=2,pady=2)



toolbar.pack(side=TOP,fill=X)
tp.pack()
root.mainloop()



