from tkinter import *
from tkinter.messagebox import showinfo
import os
from tkinter.filedialog import askopenfilename, asksaveasfilename

def newFile():
    global file
    root.title("Untitled-Notepad")
    file = None
    TextArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + "-Notepade")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
        if file=="":
            file = None
        else:
            # save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file)+ "-Notepad")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad", "Notepad by Ritik Vishvakarma")

if __name__ == '__main__':
    root = Tk()
    root.title("Untitled- Notepad")
    root.wm_iconbitmap("Martz90-Circle-Plex.ico")
    root.geometry("700x600")

    root.bind("<Control_L><o>", lambda x : openFile())

    # Add textArea
    TextArea = Text(root, font="lucida 13")
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    # Lets create a menubar
    MenuBar = Menu(root)
    # File Menu starts
    FileMenu = Menu(MenuBar, tearoff=0)
    # To open new file
    FileMenu.add_command(label="New", command=newFile)

    # To open already existing file
    FileMenu.add_command(label="Open", command=openFile)
    
    # To save the current file
    FileMenu.add_command(label="Save", command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quitApp)
    MenuBar.add_cascade(label="File", menu=FileMenu)
    # File Menu ends

    # Edit Menu starts
    EditMenu = Menu(MenuBar, tearoff=0)
    # to give a feature of cut, copy, paste
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)

    MenuBar.add_cascade(label="Edit", menu=EditMenu)
    # Edit Menu ends

    # Help Menu starts
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="About Notepad", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)
    # Help Menu ends

    root.config(menu=MenuBar)

    # Adding Scrollbar
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.bind('<Control-x>', lambda x: quitApp())
    root.mainloop()