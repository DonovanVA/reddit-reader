## Reddit reader

### Welcome to reddit-reader: This repo serves to aid text-to-speech translation for reddit posts



https://github.com/DonovanVA/reddit-reader/assets/86190604/8945853b-1d39-4370-9e99-2ada5912a492



## Getting Started:

### 1. Installation:

#### 1.1 Install the dependencies

```
pip install -r requirements.txt

```

#### 1.2 Install imagemagick
##### Installation website: https://imagemagick.org/script/download.php

##### You might want to uncomment this line in the main.py file if you are using windows or if you encounter problems with the imagemagick path not being set
```
# change_settings({"IMAGEMAGICK_BINARY": "/path/to/convert"})
```
##### where the path to convert is you zsh/bash EXPORT path


### 2. Using the script
##### The code below shows the relative parameters to be set to use the application
```
if __name__ == "__main__":
    text_file = "texts/sample.txt"  # <- Replace with the relative path to your text file to transcribe
    background_video = "backgrounds/background1.mp4" # add the background video of your choice
    output_filename = "output/output_video.mp4" # output dir of the video
    fps = 30

    text_to_video_from_file(text_file, output_filename, background_video,fps)
```

Markup : 1. Insert your background video into the /backgrounds folder
         2. Copy and paste your text into the sample.txt file (or you insert your own txt file etc)
         3. run 
         ```
         python main.py
         ```
         4. the output video will appear in the /output folder


### 3. Important notes:

##### Ensure that the video clip is long enough for your narration.
##### Adding subtitles is still unavailable, would like some help/PR to enable this feature.
##### Example Background video: https://www.youtube.com/watch?v=intRX7BRA90&t=2s - download and place it in the backgrounds folder
##### Current system:
![Screenshot 2023-09-09 at 8 10 04 PM](https://github.com/DonovanVA/reddit-reader/assets/86190604/407c77dd-a074-44b2-88bb-3df907f5cb7e)






