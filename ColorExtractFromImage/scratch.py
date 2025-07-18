import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import simpledialog
import colorgram
import os

def choose_image():
    file_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )
    if file_path:
        try:
            num_colors = simpledialog.askinteger("Number of Colors", "How many colors to extract?", minvalue=1, maxvalue=50)
            if num_colors is None:
                return

            colors = colorgram.extract(file_path, num_colors)
            color_list = [(col.rgb.r, col.rgb.g, col.rgb.b) for col in colors]

            display_colors(color_list)

        except Exception as e:
            messagebox.showerror("Error", str(e))

def display_colors(colors):
    for widget in color_frame.winfo_children():
        widget.destroy()

    for idx, (r, g, b) in enumerate(colors):
        hex_color = f'#{r:02x}{g:02x}{b:02x}'
        color_box = tk.Label(color_frame, bg=hex_color, width=10, height=2)
        color_box.grid(row=idx // 10, column=idx % 10, padx=3, pady=3)

    print("Extracted Colors (RGB):")
    for color in colors:
        print(color)

# GUI setup
root = tk.Tk()
root.title("Color Extractor")
root.geometry("600x300")
root.resizable(False, False)

title_label = tk.Label(root, text="Extract Dominant Colors from Image", font=("Arial", 14))
title_label.pack(pady=10)

choose_btn = tk.Button(root, text="Choose Image", command=choose_image, font=("Arial", 12))
choose_btn.pack(pady=5)

color_frame = tk.Frame(root)
color_frame.pack(pady=10)

root.mainloop()
