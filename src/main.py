import tkinter as tk
from ui_elements import initialize_ui
from database_operations import list_databases

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tubelizer")

    db_listbox, upload_button, tree, prev_button, next_button = initialize_ui(root)
    list_databases(db_listbox)

    root.mainloop()
