"""
This script automatically detects the language of a text file and translates
                                             it to English using the Google Translate API.
"""

import googletrans
from googletrans import Translator
from langdetect import detect

# Create a Translator object
translator = Translator()

# Prompt the user to enter the source file name
source_file = input("Enter source file (with .txt extension): ")

# Initialize the data variable
data = None

# Open the source file for reading
with open(source_file, encoding="utf8") as source_file_object:
    # Read the contents of the source file
    data = source_file_object.read()

# Detect the language of the input text
source_language = detect(data)

# Translate the text to English if it's not already in English
if source_language != 'en':
    translation = translator.translate(data, src=source_language, dest='en')
else:
    translation = data  # If the text is already in English, no need to translate

# Print the translated text
print("Detected language:", source_language)
print("Translated text:")
print(translation.text)

# Prompt the user to enter the destination file name
destination_file = input("Enter destination file (with .txt extension): ")

# Open the destination file for writing
with open(destination_file, encoding="utf8", mode="w") as destination_file_object:
    # Write the translated text to the destination file
    destination_file_object.write(translation.text)
