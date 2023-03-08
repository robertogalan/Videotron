from gtts import gTTS
import json

with open("story.json", "r") as f:
    data = json.load(f)

title = data["Title"]
paragraphs = data["Paragraphs"]

for i, paragraph in enumerate(paragraphs):
    # Create a gTTS object and save the audio file
    tts = gTTS(text=paragraph, lang="en")
    filename = f"paragraph{i+1}.mp3"
    tts.save(filename)
    print(f"Audio file {filename} generated for paragraph {i+1}")
