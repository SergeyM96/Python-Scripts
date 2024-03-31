import tkinter as tk
from tkinter import messagebox

# Define conversion factors
CONV_FACTORS = {
    "cm": 0.01,
    "m": 1.0,
    "km": 1000.0,
    "feet": 0.3048,
    "miles": 1609.344,
    "inches": 0.0254,
    "yards": 0.9144
}

# Define function to convert from one unit to another
def convert():
    try:
        # Get input value and units
        input_value = float(input_entry.get())
        input_unit = input_unit_var.get()
        output_unit = output_unit_var.get()

        # Check if input and output units are the same
        if input_unit == output_unit:
            messagebox.showwarning("Warning", "Select different units")
        else:
            # Perform conversion
            output_value = input_value * (CONV_FACTORS[input_unit] / CONV_FACTORS[output_unit])
            output_entry.delete(0, tk.END)
            output_entry.insert(0, f"{output_value:.4f}")

    except ValueError:
        messagebox.showerror("Error", "Invalid input value")

# Creation of the main window
root = tk.Tk()
root.title("Distance Unit Converter")
root.geometry("600x400")
root.resizable(False, False)

# Set window background color
root.configure(bg="#F0F0F0")

# Create input frame
input_frame = tk.Frame(root, bg="#FFFFFF", bd=2, relief=tk.RAISED)
input_frame.pack(pady=20)

input_label = tk.Label(input_frame, text="Input Value:", bg="#FFFFFF", fg="#333333", font=("Arial", 12))
input_label.grid(row=0, column=0, padx=10, pady=10)

input_entry = tk.Entry(input_frame, font=("Arial", 12), justify=tk.CENTER)
input_entry.grid(row=0, column=1, padx=10, pady=10)

input_unit_var = tk.StringVar()
input_unit_var.set("Select Unit")
input_unit_menu = tk.OptionMenu(input_frame, input_unit_var, "cm", "m", "km", "feet", "miles", "inches", "yards")
input_unit_menu.config(font=("Arial", 12))
input_unit_menu.grid(row=0, column=2, padx=10, pady=10)

# Create output frame
output_frame = tk.Frame(root, bg="#FFFFFF", bd=2, relief=tk.RAISED)
output_frame.pack(pady=20)

output_label = tk.Label(output_frame, text="Output Value:", bg="#FFFFFF", fg="#333333", font=("Arial", 12))
output_label.grid(row=0, column=0, padx=10, pady=10)

output_entry = tk.Entry(output_frame, font=("Arial", 12), justify=tk.CENTER)
output_entry.grid(row=0, column=1, padx=10, pady=10)

output_unit_var = tk.StringVar()
output_unit_var.set("Select Unit")
output_unit_menu = tk.OptionMenu(output_frame, output_unit_var, "cm", "m", "km", "feet", "miles", "inches", "yards")
output_unit_menu.config(font=("Arial", 12))
output_unit_menu.grid(row=0, column=2, padx=10, pady=10)

# Create convert button
convert_button = tk.Button(root, text="Convert", command=convert, bg="#4CAF50", fg="#FFFFFF", font=("Arial", 14), padx=20, pady=10)
convert_button.pack(pady=20)

# Run the main loop
root.mainloop()