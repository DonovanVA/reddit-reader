from moviepy.editor import *
from gtts import gTTS
import os
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.config import change_settings
from autocap import process_video
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()
# PLEASE remember to run pip install -r requirements.txt

# uncomment the line below if you are a windows user, this is to specify the path
# change_settings({"IMAGEMAGICK_BINARY": "/path/to/convert"})

# Set the temporary directory for MoviePy
change_settings({"temp_dir": "/temp"})
def add_subtitiles(subtitle_file:str,final_clip: VideoClip) -> CompositeVideoClip:
    def split_text(txt):
        # Split the text into substrings containing fewer words
        words = txt.split()
        num_words = 3  # Number of words per subtitle
        subtitles = [words[i:i+num_words] for i in range(0, len(words), num_words)]
        return [' '.join(subtitle) for subtitle in subtitles]

    generator = lambda txt: TextClip(
        txt,
        font="/fonts/Proxima_Nova_Semibold.ttf",
        fontsize=48,
        color="white",
        stroke_color="black",
        stroke_width=2,
    )

    subtitles = SubtitlesClip(subtitle_file,generator)

    # Set the position of the subtitles
    result = CompositeVideoClip([
        final_clip,
        subtitles.set_position(("center", "center"))
    ])

    return result
# Function to create a video with text overlay and narration from a text file
def text_to_video_from_file(text_file, output_filename, background_video,subtitle_file, fps):
    # Read text from the text file
    with open(text_file, 'r') as file:
        text = file.read()
    target_resolution = (1080,1920)
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
    video = video.resize(height=target_resolution[1])
    ## process subtitles from the video
    process_video("attach",video)
    # Set the position of the subtitles
    result = add_subtitiles(subtitle_file,video)
    # Write video file
    # Write the final video to the output file and set the frame rate
    result.write_videofile(output_filename, codec='libx264', audio_codec='aac', fps=fps)
    
    # Clean up the temporary audio file
    os.remove(narration_audio_file)
    os.remove(subtitle_file)

if __name__ == "__main__":
    fps = 30
    # Concatenate the timestamp to the output video filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    BACKGROUND_MEDIA = os.getenv("BACKGROUND_MEDIA")
    TEXT_FILE = os.getenv("TEXT_FILE")
    OUTPUT_VID = f"{os.getenv('OUTPUT_VID')}_timestamped_{timestamp}.mp4"
    TEMP_FILE = os.getenv("TEMP_FILE")
    OUTPUT_SRT = os.getenv("OUTPUT_SRT")
    text_to_video_from_file(TEXT_FILE,OUTPUT_VID, BACKGROUND_MEDIA,OUTPUT_SRT,fps)