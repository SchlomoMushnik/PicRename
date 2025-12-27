import tkinter as tk
from tkinter import ttk
import pandas as pd


def show_chart(df):
    """Display a DataFrame in a modern GUI window with a close button."""
    # Create root window
    root = tk.Tk()
    root.title("Data Table")
    root.geometry("1200x600")
    
    # Create frame for table
    table_frame = ttk.Frame(root)
    table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Create Treeview widget for table display
    columns = list(df.columns)
    tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=20)
    
    # Define column headings and widths
    for col in columns:
        tree.heading(col, text=col)
        # Calculate max width needed for column
        max_width = max(
            len(str(col)),
            df[col].astype(str).map(len).max()
        )
        tree.column(col, width=max_width * 8)  # 8 pixels per character
    
    # Insert data rows
    for _, row in df.iterrows():
        tree.insert("", tk.END, values=list(row))
    
    # Add scrollbars
    vsb = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=tree.yview)
    hsb = ttk.Scrollbar(table_frame, orient=tk.HORIZONTAL, command=tree.xview)
    tree.configure(yscroll=vsb.set, xscroll=hsb.set)
    
    tree.grid(row=0, column=0, sticky="nsew")
    vsb.grid(row=0, column=1, sticky="ns")
    hsb.grid(row=1, column=0, sticky="ew")
    
    table_frame.grid_rowconfigure(0, weight=1)
    table_frame.grid_columnconfigure(0, weight=1)
    
    # Create button frame
    button_frame = ttk.Frame(root)
    button_frame.pack(pady=10)
    
    # Close button
    close_button = ttk.Button(button_frame, text="Close", command=root.quit)
    close_button.pack()
    
    root.mainloop()