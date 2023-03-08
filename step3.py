import requests
import json
from PIL import Image
from io import BytesIO
import random
import os
import time

# Load the story from the JSON file
with open("story.json", "r") as f:
    story_data = json.load(f)

paragraphs = story_data["Paragraphs"]

# Set the OpenAI API endpoint URL
url = "https://api.openai.com/v1/images/generations"

# Get the OpenAI API key from an environment variable
api_key = os.environ.get("OPENAI_API_KEY")

# Set the OpenAI API headers with the API key
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Set possible art styles
art_styles = ["realism", "minimalism", "watercolors", "pastels", "retro", "vintage", "retromodern", "geometric", "vector", "flat", "3d illustration", "3d render", "3d raytracing", "surrealism", "psychedelic", "oil", "renaissance", "acrylics", "fresco", "crayons", "pen and ink", "pencil", "pixel art", "markers", "chillwave", "digital art", "3d", "graffiti", "hyperrealism", "lovecraftian", "outrun", "street art", "surreal", "synthwave", "anime", "cubism", "doge", "dreamworks", "pixar", "expressionism", "gothic", "steampunk", "cyberpunk", "powerpuff girls", "shrek", "spongebob"]

# Select a random art style
art_style = random.choice(art_styles)

# Add the art style to the story data
story_data["Art Style"] = art_style

# Generate an image for each paragraph
for i, paragraph in enumerate(paragraphs):
    # Pause for 2 seconds before generating each image
    time.sleep(2)

    # Set the prompt for the DALL-E API
    prompt = f"Generate an image of {paragraph} using Dall-E in {art_style} style. "

    # Set the parameters for the DALL-E API request
    data = {
        "model": "image-alpha-001",
        "prompt": prompt,
        "num_images": 1,
        "size": "512x512",
        "response_format": "url"
    }

    # Set the timeout in seconds
    timeout = 30

    while True:
        try:
            # Send the DALL-E API request and get the image URL from the response
            response = requests.post(url, headers=headers, data=json.dumps(data), timeout=timeout)
            image_url = response.json()["data"][0]["url"]

            # Download the image from the URL and save it as a PNG file
            response = requests.get(image_url, timeout=timeout)
            img = Image.open(BytesIO(response.content))
            filename = f"image{i+1}.png"
            img.save(filename)
            print(f"Image file {filename} generated for paragraph {i+1} in {art_style} style")
            break

        except KeyError:
            print("Error generating image. Starting over ...")

# Write the updated data to the JSON file
with open("story.json", "w") as f:
    json.dump(story_data, f, indent=4)
