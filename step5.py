import os
import json
import shutil
import zipfile

# Load the story file
with open("story.json") as f:
    data = json.load(f)

# Extract the supertitle value
outputfilename = data["Supertitle"]

# Create a list of files to be zipped
files_to_zip = [
    "image1.png",
    "image2.png",
    "image3.png",
    "image4.png",
    "image5.png",
    "paragraph1.mp3",
    "paragraph2.mp3",
    "paragraph3.mp3",
    "paragraph4.mp3",
    "paragraph5.mp3",
    "story.json",
    "audio.mp3",
    "video.mp4",
    "output.mp4"
]

# Create the zip file
zip_filename = outputfilename + ".zip"
with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zf:
    for file in files_to_zip:
        zf.write(file)

# Rename the output.mp4 file to the supertitle value
os.rename("output.mp4", outputfilename + ".mp4")

# Move the zip file and the renamed output.mp4 file to the /videos/outputfilename directory
output_dir = os.path.join("videos", outputfilename)
os.makedirs(output_dir, exist_ok=True)
shutil.move(zip_filename, os.path.join(output_dir, zip_filename))
shutil.move(outputfilename + ".mp4", os.path.join(output_dir, outputfilename + ".mp4"))

# Delete the remaining files
for file in files_to_zip:
    os.remove(file)
