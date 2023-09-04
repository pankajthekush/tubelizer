import tkinter as tk
from tkinter import ttk

def create_left_pane(root, db_listbox, list_databases, show_context_menu):
    left_frame = tk.Frame(root)
    left_frame.pack(side=tk.LEFT, fill=tk.Y)

    db_listbox.pack(side=tk.LEFT, fill=tk.Y)
    list_databases()

    db_listbox.bind("<Button-3>", show_context_menu)
    
    return left_frame

def create_right_pane(root, upload_csv, prev_page, next_page):
    right_frame = tk.Frame(root)
    right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=tk.YES)
    
    upload_button = tk.Button(right_frame, text="Upload CSV", command=upload_csv)
    upload_button.pack()
    
    frame = tk.Frame(right_frame)
    frame.pack(fill=tk.BOTH, expand=tk.YES)
    
    tree = ttk.Treeview(frame)
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)
    
    scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)
    tree.configure(yscrollcommand=scroll.set)
    
    nav_frame = tk.Frame(right_frame)
    nav_frame.pack(side=tk.BOTTOM, fill=tk.X)

    prev_button = tk.Button(nav_frame, text="Previous", command=prev_page)
    prev_button.pack(side=tk.LEFT)

    next_button = tk.Button(nav_frame, text="Next", command=next_page)
    next_button.pack(side=tk.RIGHT)

    return right_frame, tree

def create_context_menu(root, on_connect, on_disconnect):
    context_menu = tk.Menu(root, tearoff=0)
    context_menu.add_command(label="Connect", command=on_connect)
    context_menu.add_command(label="Disconnect", command=on_disconnect)
    
    return context_menu
