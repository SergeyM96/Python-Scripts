from tkinter import *
from tkinter import messagebox
from PyDictionary import PyDictionary

# Initialize Tkinter window
root = Tk()
root.title("GUI Dictionary")
root.geometry("700x500")
root.configure(bg="#f0f0f0")  # Set background color

# Initialize PyDictionary
dictionary = PyDictionary()

# Function to get meaning of the word
def getMeaning():
    word_text = word.get().strip()
    if word_text:
        response = dictionary.meaning(word_text)
        if response:
            if 'Noun' in response:
                meaning = response['Noun'][0]
            elif 'Verb' in response:
                meaning = response['Verb'][0]
            elif 'Adjective' in response:
                meaning = response['Adjective'][0]
            else:
                meaning = "No meaning found"
        else:
            meaning = "No meaning found"
    else:
        messagebox.showinfo("Error", "Please enter a word to search for.")
        return

    # Update meaning label with the result
    meaning_label.config(text=meaning, fg="#333333")

# Header Label
heading_label = Label(root, text="Dictionary", font=("Arial", 40, "bold"), fg="#333333", bg="#f0f0f0")
heading_label.pack(pady=20)

# Frame for word entry
frame = Frame(root, bg="#f0f0f0")
Label(frame, text="Enter Word", font=("Helvetica", 20), fg="#333333", bg="#f0f0f0").pack(side=LEFT)
word = Entry(frame, font=("Helvetica", 20))
word.pack(padx=10, pady=10)
frame.pack()

# Search Button
search_button = Button(root, text="Search Word", font=("Arial", 20, "bold"), relief=RIDGE, borderwidth=3,
                       cursor="hand2", fg="#ffffff", bg="#007bff", command=getMeaning)
search_button.pack(pady=10)

# Frame for displaying meaning
frame1 = Frame(root, bg="#f0f0f0")
Label(frame1, text="Meaning: ", font=("Helvetica", 20), fg="#333333", bg="#f0f0f0").pack(side=LEFT)
meaning_label = Label(frame1, text="", font=("Helvetica", 18), wraplength=600, fg="#333333", bg="#f0f0f0")
meaning_label.pack(pady=10)
frame1.pack()

# Additional Feature: Clear Button
def clearEntry():
    word.delete(0, END)
    meaning_label.config(text="")

clear_button = Button(root, text="Clear", font=("Arial", 15), relief=RIDGE, borderwidth=3,
                      cursor="hand2", fg="#ffffff", bg="#dc3545", command=clearEntry)
clear_button.pack(pady=10)

# Main loop
root.mainloop()
