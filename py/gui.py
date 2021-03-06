#!/usr/bin/env python
from get_platform import get_platform
from cmdlet import search
from config import make_urls, alias_to_browser
from tkinter import *
from tkinter import ttk

def center_window(width=300, height=200):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

def auto_search():
    keyword = keyword_obj.get()

    search_type = com.get()
    platform = get_platform()
    if platform == 'Windows':
        browser = alias_to_browser['edge']
    else:
        browser = alias_to_browser['safa']
    default_browser = browser
        
    debug = False

    browser = alias_to_browser.get(browser, default_browser)
    
    urls = make_urls(keyword, search_type, platform)
    search(urls, browser, platform, debug)
    keyword_obj.set('')


root = Tk()
root.title('Auto Search Wizard')
root.iconbitmap('Martz90-Circle-Plex.ico')
center_window(500, 300)

grid_kwargs = {
    'padx' : 5,
    # 'ipadx' : 5,
    'pady' : 5,
    # 'ipady' : 5,
    'columnspan' : 2,
    # 'rowspan' : 2,
}

frm = ttk.Frame(root, padding=(10, 5, 10, 0))
frm.grid()

ttk.Label(frm, text="Keyword").grid(column=1, row=0, sticky='w', **grid_kwargs)
keyword_obj = StringVar() 
entry_kw = ttk.Entry(frm, textvariable=keyword_obj,width=35)
entry_kw.grid(column=10, row=0, sticky='w', **grid_kwargs)

ttk.Label(frm, text="Search Type").grid(column=1, row=1, sticky='ew', **grid_kwargs)
search_type = StringVar()
com = ttk.Combobox(frm, textvariable=search_type)
com.grid(column=10, row=1, sticky='w', **grid_kwargs)  
com['value'] = ("general", "video", "ebook", "zh", "enw")
com.current(0)

ttk.Button(frm, text="Search", command=auto_search).grid(column=10, row=2, sticky='w', **grid_kwargs)

ttk.Button(frm, text="Quit", command=root.destroy ).grid(column=10, row=2, sticky='e', **grid_kwargs)

def quit_app(event):
    root.destroy()

root.bind("<Return>", lambda x: auto_search())
root.bind('<Control-x>', quit_app)
root.mainloop()