import Tkinter
from Tkinter import *
from ScrolledText import *
import tkFileDialog
import tkMessageBox

root = Tkinter.Tk(className=" TextPad")
root.geometry("800x600")
textPad = ScrolledText(root,width=150,height=200,wrap="word")

# create a menu & define functions for each menu item
def new_file():
   root.title("Untitled")
   global file
   file = None
   textPad.delete(1.0,END)
   on_content()

def open_file():
    file = tkFileDialog.askopenfile(parent=root, mode='rb', title='Select a file',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Document","*.txt"),("HTML","*.html")])
    if file != None:
        contents = file.read()
        textPad.insert('1.0', contents)
        file.close()

def save_file():
    file = tkFileDialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(("python file",".py"),("All Files","*.*")))
    if file != None:
        data = textPad.get('1.0', END+'-1c')
        file.write(data)
        file.close()

def write_to_file(file):
   try:
      content = textPad.get(1.0,'end')
      with open(file,'w')as the_file:
         the_file.write(content)
   except IOError:
      pass

def cut_file():
   textPad.event_generate("<<Cut>>")
   on_content()
   return "break"


def copy_file():
   textPad.event_generate("<<Copy>>")
   on_content()
   return "break"


def paste_file():
   textPad.event_generate("<<Paste>>")
   on_content()
   return "break"



def undo_un():
   textPad.event_generate("<<Undo>>")
   on_content()
   return "break"


def redo_re():
   textPad.event_generate("<<Redo>>")
   on_content()
   return "break"



def exit():
    if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()


def about():
    label = tkMessageBox.showinfo("About", "Just Another TextPad \n Copyright \n No rights left to reserve")


def dummy():
    print "I am a Dummy Command, I will be removed in the next step"



def get_line_number():
   output = ''
   if show_line_number.get():
      row, col = textPad.index("end").split('.')
      for i in range(1, int(row)):
         output += str(i) + '\n'
   return output



line_number_bar = Text(root,width=4,padx=3,takefocus=0,fg="white",background='#282828',border=0,state='disabled')
line_number_bar.pack(side='left',fill='y')

def on_content(event=None):
   update_line_numbers()
   update_cursor()

def update_line_numbers(event=None):
   line_numbers = get_line_number()
   line_number_bar.config(state='normal')
   line_number_bar.delete('1.0','end')
   line_number_bar.insert('1.0',line_numbers)
   line_number_bar.config(state='disabled')

show_line_number=IntVar()
show_line_number.set(1)



def update_cursor(event=None):
   row,col = textPad.index(INSERT).split('.')
   line_num,col_num = str(int (row)),str(int(col)+1) #col starts in 0
   infotext = "Line: {0} | Column: {1}".format(line_num,col_num)
   status.config(text=infotext)

status = Label(root,text = 'Line : 1 | Column: 1',bd=1,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM,fill=X)
##-----------
new = PhotoImage(file='new.gif')
copy = PhotoImage(file='copy.gif')
paste = PhotoImage(file='paste.gif')
redo = PhotoImage(file='redo.gif')
save = PhotoImage(file='save.gif')
#search = PhotoImage(file='search.gif')
undo = PhotoImage(file='undo.gif')
open = PhotoImage(file='open.gif')
cut = PhotoImage(file='cut.gif')

##-----------
menu = Menu(root)
root.config(menu=menu)
##------------
filemenu = Menu(menu,tearoff=FALSE)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New",image=new,command=new_file,compound='left')
filemenu.add_command(label="Open", command=open,image=open,compound='left')
filemenu.add_command(label="Save", command=save_file,image=save,compound='left')
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit)
##------------
editmenu = Menu(menu,tearoff=FALSE)
menu.add_cascade(label="View",menu=editmenu)
editmenu.add_cascade(label="Cut",image=cut,compound='left',command=cut)
editmenu.add_cascade(label="Copy",image=copy,compound='left',command=copy)
editmenu.add_cascade(label="Paste",image=paste,compound='left',command=paste)
editmenu.add_separator()
editmenu.add_cascade(label="Undo",image=undo,compound='left',command=undo_un)
editmenu.add_cascade(label="Redo",image=redo,compound='left',command=redo_re)
##------------
helpmenu = Menu(menu,tearoff=FALSE)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=about)
##------------
toolbar=Frame(root,bg="grey")
b1 = Button(toolbar,image=new,command=new_file)
b1.pack(side=LEFT,padx=2,pady=2)
b2 = Button(toolbar,image=open,command=open_file)
b2.pack(side=LEFT,padx=2,pady=2)
b3= Button(toolbar,image=save,command=save_file)
b3.pack(side=LEFT,padx=2,pady=2)
b4= Button(toolbar,image=undo,command=undo_un)
b4.pack(side=LEFT,padx=2,pady=2)
b5= Button(toolbar,image=redo,command=redo_re)
b5.pack(side=LEFT,padx=2,pady=2)
#b6= Button(toolbar,image=search,command=dummy)
#b6.pack(side=LEFT,padx=2,pady=2)
b7= Button(toolbar,image=cut,command=cut_file)
b7.pack(side=LEFT,padx=2,pady=2)
b8= Button(toolbar,image=copy,command=copy_file)
b8.pack(side=LEFT,padx=2,pady=2)
b9= Button(toolbar,image=paste,command=paste_file)
b9.pack(side=LEFT,padx=2,pady=2)

toolbar.pack(side=TOP,fill=X)
textPad.pack(expand='yes',fill='both')
root.mainloop()