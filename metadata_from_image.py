"""
This script extracts metadata from an image file and displays it in a GUI window.

Usage:
    1. Run the script.
    2. Enter the path to an image file manually or use the "Browse" button to select one.
    3. Click on the "Show Metadata" button to display the metadata of the selected image.

Requirements:
    - Python 3.x
    - tkinter
    - Pillow (PIL)

"""

import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
from PIL.ExifTags import TAGS


def show_metadata():
    """
    Extract metadata from the selected image and display it in a separate window.
    """
    image_path = entry.get()
    if not image_path:
        messagebox.showerror("Error", "Please enter a valid image path")
        return

    try:
        image = Image.open(image_path)
        exifdata = image.getexif()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open image: {e}")
        return

    if not exifdata:
        messagebox.showinfo("Info", "No metadata found for this image")
        return

    metadata_window = tk.Toplevel(root)
    metadata_window.title("Image Metadata")

    metadata_text = tk.Text(metadata_window, wrap="word")
    metadata_text.pack(expand=True, fill="both")

    for tag_id in exifdata:
        tagname = TAGS.get(tag_id, tag_id)
        value = exifdata.get(tag_id)
        metadata_text.insert(tk.END, f"{tagname}: {value}\n")


def browse_image():
    """
    Open a file dialog to select an image file and populate the entry field with its path.
    """
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif;*.bmp")],
        title="Select an image file",
    )
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(tk.END, file_path)


# Create the main window
root = tk.Tk()
root.title("Image Metadata Extractor")

# Label for entering image path
label = tk.Label(root, text="Enter Image Path:")
label.pack(pady=10)

# Entry field for image path
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# Button to browse and select image
browse_button = tk.Button(root, text="Browse", command=browse_image)
browse_button.pack(pady=5)

# Button to show metadata
button = tk.Button(root, text="Show Metadata", command=show_metadata)
button.pack(pady=5)

# Start the GUI event loop
root.mainloop()
