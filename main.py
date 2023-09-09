from moviepy.editor import *
from gtts import gTTS
import os
from moviepy.config import change_settings
# PLEASE remember to run pip install -r requirements.txt

# uncomment the line below if you are a windows user, this is to specify the path
# change_settings({"IMAGEMAGICK_BINARY": "/path/to/convert"})

# Set the temporary directory for MoviePy
change_settings({"temp_dir": "/temp"})

# Function to create a video with text overlay and narration from a text file
def text_to_video_from_file(text_file, output_filename, background_video, fps):
    # Read text from the text file
    with open(text_file, 'r') as file:
        text = file.read()

    # Generate narration audio from the text using gTTS (Google Text-to-Speech)
    tts = gTTS(text, lang='en', slow=False)
    narration_audio_file = 'temp/narration_audio.mp3'
    tts.save(narration_audio_file)
    
    # Load the background video
    video = VideoFileClip(background_video)

    # Load the generated narration audio
    audio = AudioFileClip(narration_audio_file)

    # Calculate the total duration of the narration audio
    total_duration = audio.duration

    # Set the audio of the background video to the narration audio
    video = video.set_audio(audio)

    # Trim the background video to match the total duration of the narration
    video = video.subclip(0, total_duration)

    # Write the final video to the output file and set the frame rate
    video.write_videofile(output_filename, codec='libx264', audio_codec='aac', fps=fps)

    # Clean up the temporary audio file
    os.remove(narration_audio_file)

if __name__ == "__main__":
    text_file = "texts/sample.txt"  # <- Replace with the relative path to your text file to transcribe
    background_video = "backgrounds/background1.mp4" # add the background video of your choice
    output_filename = "output/output_video.mp4" # output dir of the video
    fps = 30

    text_to_video_from_file(text_file, output_filename, background_video,fps)