import json
import ffmpeg
from PIL import Image
import moviepy.editor as mp

# Set the file paths
audio_files = ["paragraph1.mp3", "paragraph2.mp3", "paragraph3.mp3", "paragraph4.mp3", "paragraph5.mp3"]
audios = [mp.AudioFileClip(file) for file in audio_files]

image_files = ["image1.png", "image2.png", "image3.png", "image4.png", "image5.png"]
images = [mp.ImageClip(file).fadein(audios[i].duration/2) for i, file in enumerate(image_files)]

# Set the font and size for the subtitles
font = "Helvetica"
fontsize = 16

# Load the story file
with open("story.json") as f:
    data = json.load(f)

title = data["Title"]
art_style = data["Art Style"]
paragraphs = data["Paragraphs"]

# Add subtitles for each paragraph and create video clips for each part
parts = []
for i in range(5):
    duration = audios[i].duration
    txt_clip = mp.TextClip(txt=paragraphs[i], font=font, fontsize=24, color="white", method="caption", size=(500, 500)).set_position(("center", 450)).set_duration(duration)
    parts.append(mp.CompositeVideoClip([images[i].margin(top=0, bottom=600, left=0, right=0), txt_clip]).set_audio(audios[i]).set_duration(duration))

# Create the final video clip
final_clip = mp.concatenate_videoclips(parts)
video_size = (1080, 1920)
final_clip = final_clip.resize(video_size)#.margin(top=0, bottom=0, left=0, right=0, color=(0, 0, 0))
 
# Concatenate all audio clips
merged_audio = mp.concatenate_audioclips(audios)
merged_audio = merged_audio.set_duration(final_clip.duration)

# Write the merged audio file
merged_audio.write_audiofile("audio.mp3")
 
# Write the video file
final_clip.write_videofile("video.mp4", fps=30, codec="mpeg4")
 
# Add the new entry
data["Supertitle"] = f"{title} in {art_style} art style"

#run fffmpeg to merge audio and video and print status
print(f"Running ffmpeg to merge audio and video to output.mp4...")
video_input = ffmpeg.input('video.mp4')
audio_input = ffmpeg.input('audio.mp3')

# Merge video and audio
output = ffmpeg.output(video_input, audio_input, 'output.mp4', vcodec='copy', acodec='aac')

# Run ffmpeg command
ffmpeg.run(output)

# Write the updated JSON file
with open("story.json", "w") as f:
    json.dump(data, f)
