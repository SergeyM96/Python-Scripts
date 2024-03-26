import tkinter as tk
from tkinter import scrolledtext
import language_tool_python

"""
This program will check your Grammar mistakes and will output the results and corrections.

"""
def check_grammar():
    # Get the text from the text box
    text = text_box.get("1.0", "end-1c")

    # Initialize LanguageTool and check for grammar mistakes
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(text)
    corrected = language_tool_python.utils.correct(text, matches)
    tool.close()

    # Display original text and corrections in the result box
    result_box.delete(1.0, tk.END)
    result_box.insert(tk.END, "Original Text:\n")
    result_box.insert(tk.END, text + "\n\n")

    result_box.insert(tk.END, "Grammar mistakes & Improvements:\n")
    for match in matches:
        incorrect_text = match.sentence.replace(match.matchedText, f"{match.matchedText}")
        suggestion = match.replacements[0] if match.replacements else "No suggestions"
        result_box.insert(tk.END, f"{match.message} => {incorrect_text}\n")
        result_box.insert(tk.END, f"Suggestion: {suggestion}\n\n")

    # Display corrected text
    result_box.insert(tk.END, "Corrected Text:\n")
    result_box.insert(tk.END, corrected)

# Create a Tkinter window
window = tk.Tk()
window.title("Grammar Checker")
window.geometry("800x600")

# Create a label above the text box
text_label = tk.Label(window, text="Put your text here", font=("Arial", 12))
text_label.pack(pady=5)

# Create a text box for user input
text_box = scrolledtext.ScrolledText(window, width=80, height=15, wrap=tk.WORD)
text_box.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

# Create a button to check grammar
check_button = tk.Button(window, text="Check Grammar", command=check_grammar)
check_button.pack(pady=5)

# Create a text area to display the results
result_box = scrolledtext.ScrolledText(window, width=80, height=15, wrap=tk.WORD)
result_box.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

# Run the Tkinter event loop
window.mainloop()
