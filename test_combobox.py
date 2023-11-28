import tkinter as tk
from tkinter import ttk

class Windows:
    def __init__(self, root):
        self.root = root
        self.root.title("Combobox Example")

        # Create a StringVar to store the selected value of the first combobox
        self.combo_var = tk.StringVar()

        # Create the first combobox
        self.first_combo = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"], textvariable=self.combo_var)
        self.first_combo.grid(row=0, column=0, padx=10, pady=10)
        self.first_combo.set("Option 1")  # Set default value

        # Create the second combobox
        self.second_combo = ttk.Combobox(root, values=[], state="readonly")
        self.second_combo.grid(row=0, column=1, padx=10, pady=10)

        # Bind the update function to the <<ComboboxSelected>> event of the first combobox
        self.first_combo.bind("<<ComboboxSelected>>", self.update_second_combobox)

    def update_second_combobox(self, event):
        # Get the selected value from the first combobox
        selected_value = self.combo_var.get()

        # Update the options of the second combobox based on the selected value
        second_combo_values = self.generate_second_combo_options(selected_value)
        self.second_combo['values'] = second_combo_values

    def generate_second_combo_options(self, selected_value):
        # Replace this logic with your own to generate options dynamically
        if selected_value == "Option 1":
            return ["A", "B", "C"]
        elif selected_value == "Option 2":
            return ["X", "Y", "Z"]
        else:
            return []

def main():
    # Create the main window
    root = tk.Tk()

    # Create an instance of the Windows class
    app = Windows(root)

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
