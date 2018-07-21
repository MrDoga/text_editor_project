from Tkinter import *
import Tkinter as tk
import ScrolledText
import tkFileDialog as fd
import tkMessageBox
import os
PROGRAM_NAME = "Text Pad"
root = tk.Tk()
root.title(PROGRAM_NAME)
file_name = None
root.geometry('800x400')
#functions

def dummy():
    tkMessageBox.showinfo("Dummy","No Function is added yet")

def new_file():
   root.title("Untitled")
   global file_name
   file_name = None
   context_text.delete(1.0,END)
   on_content()

def open():
   input_file_name = fd.askopenfile(defaultextensio=".txt",filetypes=[("All Files","*.*"),("Text Document","*.txt"),("HTML","*.html")])
   if file:
      global file_name
      file_name = input_file_name
      root.title('{} - {}'.format(os.path.basename(file_name),PROGRAM_NAME ))
      context_text.delete(1.0,END)
      with open(file_name)as _file:
         context_text.insert(1.0, _file.read())
   on_content()

def save_as():
  input_file_name = fd.asksaveasfilename(defaultextension=".txt",filetypes=[("All Files","*.*")])
  if input_file_name:
     global file_name
     file_name = input_file_name
     write_to_file(file_name)
     root.title('{} - {}'.format(os.path.basename(file_name),PROGRAM_NAME))
  return "break"


def save():
   global file_name
   if not file_name:
      save_as()
   else:
      write_to_file(file_name)
   return "break"


def write_to_file(file_name):
   try:
      content = context_text.get(1.0,'end')
      with open(file_name,'w')as the_file:
         the_file.write(content)
   except IOError:
      pass


def exit():
   if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
      root.destroy()


def about():
   label = tkMessageBox.showinfo("About", "Just Another TextPad \n Copyright \n No rights left to reserve")


def cut():
   context_text.event_generate("<<Cut>>")
   on_content()
   return "break"


def copy():
   context_text.event_generate("<<Copy>>")
   on_content()
   return "break"


def paste_file():
   context_text.event_generate("<<Paste>>")
   on_content()
   return "break"


def undo():
   context_text.event_generate("<<Undo>>")
   on_content()
   return "break"


def redo():
   context_text.event_generate("<<>Redo>")
   on_content()
   return "break"

def selectall(event=None):
   context_text.tag_add('sel','1.0','end')
   on_content()
   return "break"


def find_text(event=None):
   search_toplevel = Toplevel(root)
   search_toplevel.title('Find Text')
   search_toplevel.transient(root)
   search_toplevel.resizable(False,False)
   Label(search_toplevel,text="Find All:").grid(rows=0,column=0,sticky='e')
   search_entry_widget = Entry(search_toplevel,width=25)
   search_entry_widget.grid(row=0,column=0,padx=2,pady=2,sticky='we')
   search_entry_widget.focus_set()
   ignore_case_value = IntVar()
   chk = Checkbutton (search_toplevel,text='Ignore Case',variable=ignore_case_value).grid(rows=1,column=1,padx=2,pady=2)
   bu = Button (search_toplevel,text="Find All",underline=0,
                command=lambda:search_output(
                   search_entry_widget.get(),ignore_case_value.get(),
                   context_text,search_toplevel,search_entry_widget)
                ).grid(row=0,column=0,sticky='e'+'w',padx=2,pady=2)

   def close_search_window():
      context_text.tag_remove('match','1.0',END)
      search_toplevel.destroy()
   search_toplevel.protocol('WM_DELETE_WINDOW',close_search_window)
   return "break"

def search_output(needle,if_ignore_case,context_text,seach_toplevel,search_box):
   context_text.tag_remove('match',1.0,END)
   matches_found=0
   if needle:
      start_pos='1.0'
      while True:
         start_pos = context_text.search(needle,start_pos,nocase=if_ignore_case,stopindex=END)
         if not start_pos:
            break

         end_pos = '() + ()c'.format(start_pos,len(needle))
         context_text.tag_add('match',start_pos,end_pos)
         matches_found +=1
         start_pos = end_pos
         context_text.tag_config('match',background='yellow',foreground='blue')
   search_box.fofocus_set()
   seach_toplevel.title('{} matches found'.format(matches_found))

# adding line number functionality
def get_line_number():
   output = ''
   if show_line_number.get():
      row,col = context_text.index("end").split('.')
      for i in range(1,int(row)):
         output += str(i) + '\n'
   return output


def on_content(event=None):
   update_line_numbers()
   update_cursor()

def update_line_numbers(event=None):
   line_numbers = get_line_number()
   line_number_bar.config(state='normal')
   line_number_bar.delete('1.0','end')
   line_number_bar.insert('1.0',line_numbers)
   line_number_bar.config(state='disabled')




def show_cursor():
   show_cursor_info_checked = show_cursor_info.get()
   if show_cursor_info_checked:
      cursor_info_bar.pack(expand='no',fill=None,side='right',anchor='se')
   else:
      cursor_info_bar.pack_forgot()

def update_cursor(event=None):
   row,col = context_text.index(INSERT).split('.')
   line_num,col_num = str(int (row)),str(int(col)+1) #col starts in 0
   infotext = "Line: {0} | Column: {1}".format(line_num,col_num)
   cursor_info_bar.config(text=infotext)

def highlight_line(interval=100):
   context_text.tag_remove("active_line",1.0,"end")
   context_text.tag_add("active_line","insert linestart","insert lineend+1c")
   context_text.after(interval,toggle_highlight)

def undo_highlight():
   context_text.tag_remove("active_line",1.0,"end")

def toggle_highlight():
   if to_highlight_line.get():
      highlight_line()
   else:
      undo_highlight()



def show_popup_menu(event):
   popup_menu.tk_popup(event.x_root,event.y_root)



new = PhotoImage(file='new.gif')
copy = PhotoImage(file='copy.gif')
paste = PhotoImage(file='paste.gif')
redo = PhotoImage(file='redo.gif')
save = PhotoImage(file='save.gif')
search = PhotoImage(file='search.gif')
undo = PhotoImage(file='undo.gif')
open = PhotoImage(file='open.gif')
cut = PhotoImage(file='cut.gif')


##menubar###
# Insert a menu bar on the main window
menu_bar = Menu(root)

file_menu = Menu(menu_bar,tearoff=0)
file_menu.add_command(label='New',accelerator='Ctrl+N',compound='left',image=new,underline=0,command=new_file)
file_menu.add_command(label='Open',accelerator='Ctrl+O',compound='left',image=new,underline=0,command=open)
file_menu.add_command(label='Save',accelerator='Ctrl+S',compound='left',image=new,underline=0,command=save)
file_menu.add_command(label='SaveAs',accelerator='Ctrl+Shift+S',compound='left',image=new,underline=0,command=save_as)
file_menu.add_separator()
file_menu.add_command(label='Exit',accelerator='Ctrl+Shift+S',compound='left',image=new,underline=0,command=exit)
menu_bar.add_cascade(label="File",menu=file_menu)

edit_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='Edit',menu=edit_menu)
edit_menu.add_cascade(label='Undo',command=dummy)
edit_menu.add_separator()
edit_menu.add_cascade(label='Redo',command=dummy)
edit_menu.add_cascade(label='Cut',command=cut)
edit_menu.add_separator()
edit_menu.add_cascade(label='Copy',command=copy)
edit_menu.add_cascade(label='Paste',command=paste_file)


view_menu = Menu(menu_bar,tearoff=0)
show_line_number=IntVar()
show_line_number.set(1)
view_menu.add_cascade(label='View',menu=view_menu)
view_menu.add_checkbutton(label='Show NumberLine',variable=show_line_number)
show_cursor_info = IntVar()
show_cursor_info.set(1)
view_menu.add_checkbutton(label="Show Cursor",variable=show_cursor_info,command=show_cursor)
to_highlight_line = IntVar()
view_menu.add_checkbutton(label="highlight line",variable=to_highlight_line,command=toggle_highlight(), onvalue=1, offvalue=0)

about_menu = Menu(menu_bar,tearoff=0)
about_menu.add_cascade(label="About",menu=about_menu)
about_menu.add_command(label="About...", command=about)

shortcut_bar = Frame(root,height=20)
shortcut_bar.pack(expand='no',fill='x')
###ToolBar###
icons = ('new','open','copy','paste','cut','redo','undo','save','search')
for i,icon in enumerate(icons):
    tool_bar_icons = PhotoImage(file='{}.gif'.format(icon))
    cmd = eval(icon)
    tool_bar = Button(shortcut_bar,image=tool_bar_icons,height=20,width=20,command=cmd)
    tool_bar.image = tool_bar_icons
    tool_bar.pack(side='left')

line_number_bar = Text(root,width=4,padx=3,takefocus=0,fg="white",background='#282828',border=0,state='disabled',wrap='none')
line_number_bar.pack(side='left',fill='y')

context_text = Text(root,wrap="word")
context_text.pack(expand='yes',fill='both')


scroll_bar = Scrollbar(context_text)
context_text.configure(yscrollcommand=scroll_bar.set,xscrollcommand=scroll_bar.set)
scroll_bar.config(command=context_text.yview)
scroll_bar.config(command=context_text.xview)
scroll_bar.pack(side='right',fill='y')


#for cursor
cursor_info_bar = Label(context_text,text = 'Line : 1 | Column: 1')
cursor_info_bar.pack(expand='no',fill=None,side='right',anchor='se')


popup_menu = Menu(context_text)
for i in ('cut','copy','paste','undo','redo'):
   cmd=eval(i)
   popup_menu.add_command(Label=i,compounds='left',command=cmd)
popup_menu.add_seperator()
popup_menu.add_command(Label='Select All', underline=7,command=selectall)
context_text.bind('<Button-3>',show_popup_menu)

root.protocol('WM_DELETE_WINDOW',exit)
root.mainloop()



