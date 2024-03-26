import moviepy.editor

"""
Extract audio from a video script
"""

# Enter the path of the video
path_video = input("Enter the path of video: ")

# Loading the video file specified by the user
video = moviepy.editor.VideoFileClip(path_video)

# Extracting audio from the loaded video
audio = video.audio

# Enter the path where you want to save the extracted audio
path_audio = input("Enter the path of audio:")

# Writing the extracted audio to the specified path
audio.write_audiofile(path_audio)
