import Tkinter
import ScrolledText # For scrolling
root = Tkinter.Tk(className=" Just another Text Editor")
textPad = ScrolledText.ScrolledText(root, width=100, height=80)
textPad.pack()
root.mainloop()
