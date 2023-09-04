import os
import tkinter as tk
from tkinter import filedialog, ttk
from .db_operations import create_db_and_insert_data,fetch_data_from_db,get_total_rows
from .csv_operations import read_data,create_db_and_insert_data
from .ui_components import create_context_menu,create_left_pane,create_right_pane

class CSVViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CSV Viewer")

        self.current_row = 0
        self.row_increment = 100

        self.db_listbox = tk.Listbox(self.root)
        self.initUI()

    def initUI(self):
        self.left_frame = create_left_pane(
            self.root, self.db_listbox, self.list_databases, self.show_context_menu)
        
        self.right_frame, self.tree = create_right_pane(
            self.root, self.upload_csv, self.prev_page, self.next_page)
        
        self.context_menu = create_context_menu(
            self.root, self.on_connect, self.on_disconnect)

    def list_databases(self):
        db_files = [f for f in os.listdir('.') if f.endswith('.db')]
        self.db_listbox.delete(0, tk.END)
        for db in db_files:
            self.db_listbox.insert(tk.END, db)

    def show_context_menu(self, event):
        self.context_menu.tk_popup(event.x_root, event.y_root)

    def upload_csv(self):
        self.current_row = 0
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return
        try:
            read_data(file_path)
            self.display_data()
        except ValueError as e:
            print(f"Error: {e}")

    def display_data(self):
        subset = fetch_data_from_db(self.current_row, self.row_increment)
        
        self.tree.delete(*self.tree.get_children())
        self.tree['columns'] = []
        
        self.tree['show'] = 'headings'
        
        self.tree["columns"] = list(subset.columns)
        for column in subset.columns:
            self.tree.column(column, width=100)
            self.tree.heading(column, text=column)
        
        for index, row in subset.iterrows():
            self.tree.insert("", index, values=list(row))

    def next_page(self):
        total_rows = get_total_rows()
        if self.current_row + self.row_increment < total_rows:
            self.current_row += self.row_increment
            self.display_data()
        else:
            print("Reached the end of the CSV file.")

    def prev_page(self):
        self.current_row = max(0, self.current_row - self.row_increment)
        self.display_data()

    def on_connect(self):
        self.current_row = 0
        selected_db = self.db_listbox.get(tk.ACTIVE)
        if selected_db:
            self.display_data()

    def on_disconnect(self):
        self.tree.delete(*self.tree.get_children())
        self.tree['columns'] = []

def start_app():
    root = tk.Tk()
    app = CSVViewerApp(root)
    root.mainloop()
