import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
import pandas as pd

window = tk.Tk()
window.title('Sistem Informasi Universitas di Indonesia')
window.geometry('1024x640')
window.resizable(False, False)
window.config(bg='#FFE8C5')

siudin_title = tk.Label(window, text="SIUDIN", fg="#BE6557", bg="#FFE8C5", font=("Sketch Bego Fill", 125))
siudin_title.grid(row=3, column=1,padx=20, sticky="w")

subjudul = tk.Label(window, text="Sistem Informasi Universitas di Indonesia", fg="black", bg="#FFE8C5",
                    font=("Letters for Learners", 35))
subjudul.grid(row=5, column=1, padx=20, sticky="w")

combo_frame = tk.Frame(window, bg="#FFE8C5")
combo_frame.grid(row=6, column=1, padx=10,sticky="w")

def load_universities():
    universities = [
        "Universitas Negeri Surabaya (UNESA)",
        "Universitas Negeri Jember (UNEJ)",
        "Universitas Negeri Malang (UM)",
        "Universitas Airlangga (UNAIR)",
        "Universitas Brawijaya (UB)",
        "Universitas Trunojoyo Madura (UTM)",
        "Universitas Pembangunan Nasional Veteran Jawa Timur (UPNV Jatim)",
        "Institut Teknologi Sepuluh Nopember (ITS)"
    ]
    return universities

def show_university_info_window(search_term):
    csv_files = {
        "Universitas Negeri Surabaya (UNESA)": "unesa.csv",
        "Universitas Negeri Jember (UNEJ)": "unej.csv",
        "Universitas Negeri Malang (UM)": "um.csv",
        "Universitas Airlangga (UNAIR)": "unair.csv",
        "Universitas Brawijaya (UB)":"ub.csv",
        "Universitas Trunojoyo Madura (UTM)":"utm.csv",
        "Universitas Pembangunan Nasional Veteran Jawa Timur (UPNV Jatim)":"upnvjt.csv",
        "Institut Teknologi Sepuluh Nopember (ITS)": "its.csv"
    }
    csv_file = csv_files.get(search_term)
    if csv_file:
        display_csv_info(csv_file)
    else:
        showerror("University Not Found", "University data not available.")

universities = load_universities()
combo_label = tk.Label(combo_frame, text="Select University: ", bg="#FFE8C5", font=("Letters for Learners", 35))
combo_label.grid(row=0, column=0, padx=10,sticky="w")

university_combo = ttk.Combobox(combo_frame, width=50, values=universities, font=('Letters for Learners', 15), state="readonly")
university_combo.grid(row=0, column=1, pady=10,sticky="w")
university_combo.bind("<<ComboboxSelected>>", lambda event: show_university_info_window(university_combo.get()))

def display_csv_info(csv_file):
    try:
        # Read CSV file using pandas
        df = pd.read_csv(csv_file)
        
        # Create new window for displaying CSV data
        info_window = tk.Toplevel(window)
        info_window.title("Sstem Informasi Universitas di Indonesia")
        info_window.geometry('800x600')
        info_window.config(bg='#FFE8C5')

        # Create search frame
        search_frame = tk.Frame(info_window, bg="#FFE8C5")
        search_frame.pack(side="top", fill="x", padx=10, pady=10)

        # Create search entry
        search_var = tk.StringVar()
        search_entry = tk.Entry(search_frame, width=50, textvariable=search_var)
        search_entry.pack(side="left", padx=5)

        # Create search button
        search_button = tk.Button(search_frame, text="Search", command=lambda: execute_search(search_var.get()))
        search_button.pack(side="left", padx=5)

        # Create ComboBox for sortiran
        sortiran_combo = ttk.Combobox(search_frame, width=30, font=('Letters for Learners', 12), state="readonly")
        sortiran_combo['values'] = tuple(df.columns)
        sortiran_combo.pack(side="left", padx=5)

        # Function to apply sortiran
        def apply_sortiran():
            sortiran_column = sortiran_combo.get()
            if sortiran_column:
                sorted_df = df.sort_values(by=sortiran_column)
                # Clear existing data in Treeview
                tree.delete(*tree.get_children())
                # Insert sorted data into Treeview
                for index, row in sorted_df.iterrows():
                    tree.insert("", "end", values=tuple(row))
            else:
                showerror("Sortiran Column Not Selected", "Please select a column to sort by.")

        # Create apply button
        apply_sortiran_button = tk.Button(search_frame, text="Apply", command=apply_sortiran)
        apply_sortiran_button.pack(side="left", padx=5)

        # Create Treeview widget to display data
        tree = ttk.Treeview(info_window)

        # Set columns based on CSV columns
        columns = tuple(df.columns)
        tree["columns"] = columns

        # Set headings for columns
        for col in columns:
            tree.heading(col, text=col)

        # Insert data into Treeview
        for index, row in df.iterrows():
            tree.insert("", "end", values=tuple(row))

        tree.pack(expand=True, fill='both')

        def execute_search(search_term):
            if search_term:
                search_result = df[df.apply(lambda row: any(search_term.lower() in str(cell).lower() for cell in row), axis=1)]
                update_treeview(tree, search_result)
            else:
                update_treeview(tree, df)

        def execute_apply(search_term):
            execute_search(search_term)  # You can apply any additional processing here if needed

    except FileNotFoundError:
        showerror("File Not Found", f"The file {csv_file} was not found.")
    except Exception as e:
        showerror("Error", f"An error occurred: {e}")

def update_treeview(tree, df):
    # Clear existing items
    tree.delete(*tree.get_children())
    
    # Insert new data into Treeview
    for index, row in df.iterrows():
        tree.insert("", "end", values=tuple(row))

window.mainloop()