import tkinter as tk
from tkinter import filedialog, messagebox #Importing necessary modules
import threading
import speech_recognition as sr
from pydub import AudioSegment
import os

class AudioToTextConverter:
    def __init__(self):
        self.root = tk.Tk()  # Initializing tkinter root window
        self.root.title("Audio to Text Converter")  # Setting window title
        self.setup_window()  # Setting up the GUI window
        self.recognizer = sr.Recognizer()  # Initializing SpeechRecognition recognizer

    def setup_window(self):
        # Function to set up the GUI window
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 300
        window_height = 200
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")  # Setting window size and position

        # Creating and placing buttons for various functions
        self.record_btn = tk.Button(self.root, text="Record", command=self.record_audio)
        self.record_btn.pack(pady=10)

        self.stop_btn = tk.Button(self.root, text="Stop", command=self.stop_recording, state=tk.DISABLED)
        self.stop_btn.pack(pady=5)

        self.upload_btn = tk.Button(self.root, text="Upload Audio File", command=self.upload_audio)
        self.upload_btn.pack(pady=5)

        self.convert_btn = tk.Button(self.root, text="Convert", command=self.convert_audio, state=tk.DISABLED)
        self.convert_btn.pack(pady=5)

        # Adjusting the position of the convert button
        self.convert_btn.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

    def record_audio(self):
        # Function to record audio
        self.record_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.convert_btn.config(state=tk.DISABLED)

        self.audio_data = None

        # Starting a new thread for recording audio
        self.recording_thread = threading.Thread(target=self.start_recording)
        self.recording_thread.start()

    def start_recording(self):
        # Function to start recording audio
        with sr.Microphone() as source:
            print("Recording...")
            self.audio_data = self.recognizer.record(source, duration=15)
            print("Recording stopped")

    def stop_recording(self):
        # Function to stop recording
        self.recording_thread.join()
        self.record_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self.convert_btn.config(state=tk.NORMAL)

        messagebox.showinfo("Success", "Stopped recording, press 'Convert' button to proceed")

    def convert_audio(self):
        # Function to convert audio to text
        if self.audio_data:
            try:
                text = self.recognizer.recognize_google(self.audio_data)
                self.save_text_to_file(text)
                messagebox.showinfo("Success", "Conversion was successful. Text file saved!")
            except sr.UnknownValueError:
                messagebox.showerror("Error", "Could not understand audio")
            except sr.RequestError as e:
                messagebox.showerror("Error", f"Could not request results from Google Speech Recognition service: {e}")
        else:
            messagebox.showerror("Error", "No audio data recorded")

    def save_text_to_file(self, text):
        # Function to save text to a file
        script_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_directory, "converted_text.txt")
        with open(file_path, "w") as text_file:
            text_file.write(text)

    def upload_audio(self):
        # Function to upload audio file
        file_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.wav;*.mp3")])
        if file_path:
            try:
                self.process_uploaded_audio(file_path)
                self.convert_btn.config(state=tk.NORMAL)  # Enable the "Convert" button after uploading the file
                messagebox.showinfo("Success", "Audio file uploaded successfully! Press 'Convert' to proceed.")
            except Exception as e:
                messagebox.showerror("Error", f"Error while processing the audio file: {str(e)}")
        else:
            messagebox.showerror("Error", "No file selected")

    def process_uploaded_audio(self, file_path):
        # Function to process uploaded audio file
        self.audio_data = None
        if file_path.lower().endswith('.wav'):
            with sr.AudioFile(file_path) as source:
                self.audio_data = self.recognizer.record(source)
        elif file_path.lower().endswith('.mp3'):
            audio = AudioSegment.from_mp3(file_path)
            with open(file_path[:-4] + ".wav", "wb") as wav_file:
                audio.export(wav_file, format="wav")
            with sr.AudioFile(file_path[:-4] + ".wav") as source:
                self.audio_data = self.recognizer.record(source)
            os.remove(file_path[:-4] + ".wav")
        else:
            messagebox.showerror("Error", "Unsupported file format. Please select a WAV or MP3 file.")

if __name__ == "__main__":
    # Creating an instance of the AudioToTextConverter class and starting the Tkinter event loop
    AudioToTextConverter().root.mainloop()
