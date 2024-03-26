import tkinter as tk
from tkinter import ttk
from gtts import gTTS
from deep_translator import GoogleTranslator
import os
from tkinter import messagebox

"""
A script that saves voice record of the text you write in mp3 to your scripts directory
"""

def speak_text():
    text = text_entry.get("1.0", "end-1c")
    selected_language = lang_var.get()
    if selected_language == "":
        messagebox.showwarning("No Language Selected", "Please select a language before saving and speaking.")
        return

    language = languages[selected_language]

    translator = GoogleTranslator(source='auto', target=language)
    translated_text = translator.translate(text)

    # Use gTTS to synthesize speech
    tts = gTTS(text=translated_text, lang=language, slow=False, tld='com', lang_check=True)
    tts.save("temp.mp3")

    # Play the synthesized speech
    os.system("start temp.mp3")


# Create the root window
root = tk.Tk()
root.title("Text-to-Speech")

# Use a modern theme
style = ttk.Style()
style.theme_use('vista')

# Calculate the position to center the window
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set the geometry to center the window
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create main frame
main_frame = ttk.Frame(root, padding=10)
main_frame.grid(row=0, column=0, sticky="nsew")

# Create text frame
text_frame = ttk.LabelFrame(main_frame, text="Enter Text", padding=10)
text_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

# Create text entry widget
text_entry = tk.Text(text_frame, height=5, width=30)
text_entry.grid(row=0, column=0, sticky="nsew")

# Create options frame
options_frame = ttk.LabelFrame(main_frame, text="Options", padding=10)
options_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

# Create language label
lang_label = ttk.Label(options_frame, text="Choose language:")
lang_label.grid(row=0, column=0, sticky="w")

# Define supported languages
languages = {
    "English (US)": "en",
    "Hebrew": "iw",
    "Russian": "ru",
    "Arabic": "ar",
    # Add more languages as needed
}

# Create language variable and dropdown
lang_var = tk.StringVar()
lang_dropdown = ttk.Combobox(options_frame, textvariable=lang_var, values=list(languages.keys()), state="readonly")
lang_dropdown.grid(row=0, column=1, sticky="w")

# Create speak button
speak_button = ttk.Button(root, text="Save & Speak", command=speak_text)
speak_button.grid(row=2, column=0, pady=10)

# Start the tkinter event loop
root.mainloop()
