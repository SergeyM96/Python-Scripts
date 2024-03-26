import requests
from bs4 import BeautifulSoup
from tkinter import *
"""
This app will Scrap the lyrics of a song that you input.
"""

def get_lyrics(artist, song):
    """
    Get the lyrics of a song by artist from azlyrics.com and return them.

    Args:
        artist (str): The name of the artist or band.
        song (str): The name of the song.

    Returns:
        str: The lyrics of the song.
    """
    # Construct the URL
    song_url = f'http://www.azlyrics.com/lyrics/{artist}/{song}.html'

    # Send a GET request to the URL
    response = requests.get(song_url)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    try:
        # Find the lyrics section and extract them
        lyrics = soup.find('div', class_='col-xs-12 col-lg-8 text-center').find_all('div')[5].text.strip()
        return lyrics
    except AttributeError:
        return "Lyrics not found. Please make sure you have entered the correct name (i.e., don't add spaces between words)!"


def display_lyrics_window(lyrics):
    """
    Display the lyrics in a new window.

    Args:
        lyrics (str): The lyrics to display.
    """
    lyrics_window = Tk()
    lyrics_window.title("Lyrics")
    lyrics_window.geometry("600x400")

    # Center the window on the screen
    center_window(lyrics_window)

    scrollbar = Scrollbar(lyrics_window)
    scrollbar.pack(side=RIGHT, fill=Y)

    lyrics_text = Text(lyrics_window, wrap=WORD, yscrollcommand=scrollbar.set)
    lyrics_text.insert(END, lyrics)
    lyrics_text.pack(expand=True, fill=BOTH)

    scrollbar.config(command=lyrics_text.yview)

    lyrics_window.mainloop()


# Create a GUI
root = Tk()
root.geometry("400x200")
root.resizable(True, True)
root.title("Lyrics Finder")


def center_window(window):
    # Get screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate x and y coordinates for the window to center it
    x = (screen_width - window.winfo_reqwidth()) // 2
    y = (screen_height - window.winfo_reqheight()) // 2

    # Set the window geometry
    window.geometry(f"+{x}+{y}")


# Center the window on the screen
center_window(root)

# Artist input
artist_label = Label(root, text="Enter the name of the artist/band:")
artist_label.pack(pady=5)
artist_entry = Entry(root)
artist_entry.pack(pady=5)

# Song input
song_label = Label(root, text="Enter the name of the song:")
song_label.pack(pady=5)
song_entry = Entry(root)
song_entry.pack(pady=5)


def get_lyrics_gui():
    artist = artist_entry.get().strip().lower().replace(' ', '')
    song = song_entry.get().strip().lower().replace(' ', '')
    lyrics = get_lyrics(artist, song)
    display_lyrics_window(lyrics)


# Search button
search_button = Button(root, text="Search", command=get_lyrics_gui)
search_button.pack(pady=10)

root.mainloop()
