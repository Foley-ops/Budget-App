import tkinter as tk
from tkinter import ttk
import sqlite3
import matplotlib.pyplot as plt
import pandas as pd  # or openpyxl

from DatabaseManager import DatabaseManager

# GUI setup
class BudgetApp:
    def __init__(self, root):
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        self.root.geometry("600x400")
        self.root.title("BudgetApp")

        self.notebook = ttk.Notebook(self.root)

        # Create tabs with a frame to hold the fields and their corresponding lists
        self.tabs = {
            'Income': ([], tk.Frame(self.notebook)),
            'Bills': ([], tk.Frame(self.notebook)),
            'Expenses': ([], tk.Frame(self.notebook)),
            'Savings': ([], tk.Frame(self.notebook))
        }

        for tab_name, (field_list, frame) in self.tabs.items():
            self.notebook.add(frame, text=tab_name)

        self.notebook.pack(expand=True, fill='both')

        # General Add and Delete buttons
        tk.Button(self.root, text="Add Field", command=self.add_field).pack(side=tk.LEFT)
        tk.Button(self.root, text="Delete Last Field", command=self.delete_last_field).pack(side=tk.LEFT)
        
        # Initialize each tab with one open field
        for tab_name in self.tabs:
            self.notebook.select(self.tabs[tab_name][1])  # Select tab
            self.add_field()  # Add initial field

        self.notebook.select(self.tabs['Income'][1])  # Re-select the first tab


    def add_field(self):
        # Add a field to the currently selected tab
        tab_name = self.notebook.tab(self.notebook.select(), "text")
        field_list, frame = self.tabs[tab_name]

        field_vars = {}

        new_field = tk.Frame(frame)
        
        name_var = tk.StringVar()
        tk.Label(new_field, text=f'Name:').pack(side=tk.LEFT)
        tk.Entry(new_field, textvariable=name_var).pack(side=tk.LEFT)
        field_vars['name'] = name_var  # Save the StringVar
        
        amount_var = tk.StringVar()
        tk.Label(new_field, text='Amount:').pack(side=tk.LEFT)
        amount_entry = tk.Entry(new_field, textvariable=amount_var)
        amount_entry.pack(side=tk.LEFT)
        field_vars['amount'] = amount_var  # Save the StringVar
        # Allow only numeric input for amount
        self.validate_numeric_entry(amount_entry)
        
        # Add interest rate field for Bills and Savings tabs
        if tab_name in ['Bills', 'Savings']:
            interest_var = tk.StringVar()
            tk.Label(new_field, text='Interest Rate (%):').pack(side=tk.LEFT)
            interest_rate = tk.Entry(new_field, textvariable=interest_var)
            interest_rate.insert(0, "0")  # Default value
            interest_rate.pack(side=tk.LEFT)
            field_vars['interest'] = interest_var  # Save the StringVar
            # Allow only numeric input for interest
            self.validate_numeric_entry(interest_rate)
        
        new_field.pack()

        field_list.append(new_field)

    def delete_last_field(self):
        # Delete the last field in the currently selected tab
        tab_name = self.notebook.tab(self.notebook.select(), "text")
        field_list, frame = self.tabs[tab_name]

        if field_list:
            field_list[-1].destroy()
            field_list.pop()

    def calculate_savings_growth(self):
        # Logic to calculate savings growth
        pass

    def display_pie_chart(self):
        # Logic to display pie chart for income/bills/expenses
        pass

    def display_savings_graph(self):
        # Logic to display graph for savings over time
        pass

    def save_data_to_db(self):
        # Logic to save current state to database
        pass

    def load_data_from_db(self):
        # Logic to load data from database
        pass

    def export_data_to_spreadsheet(self):
        # Logic to export data to a spreadsheet
        pass
    
    def validate_numeric_entry(self, entry):
        # Allow only digits and a single dot in the entry field
        def validate(char, entry_value):
            if char in '0123456789.':
                if char == '.' and '.' in entry_value:
                    return False
                return True
            return False

        validate_command = (self.root.register(validate), '%S', '%P')
        entry.configure(validate='key', validatecommand=validate_command)
    
    
if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetApp(root)
    root.mainloop()