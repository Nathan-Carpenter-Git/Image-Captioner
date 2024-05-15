# Image Captioner

## About
Very lightweight image captioner for Spyfall Discord bot. Used to quickly caption a large amount of images centered around compatibility with the Spyfall Discord bot. [link](https://github.com/Nathan-Carpenter-Git/spyfall-discord-bot/tree/main)

## Prerequisites
- Install Python. [Link](https://www.python.org/downloads/)
- Install Pillow. [Link](https://pillow.readthedocs.io/en/stable/installation/basic-installation.html)

## How-to-use
- Find images online for locations you want. I recommend adding "cartoon" at the end of the search to give the desired "Spyfall effect." (Make sure they are all PNGs)
- Rename all images into an order (0.png | 1.png | etc.)
- Replace locations array in ImageCaption.py with the names of the locations in same order as the images. (locations = ["Airport Terminal", "Avengers Movie", etc.])
- Run ImageCaption.py with Python (python ImageCaption.py) using a CLI (Powershell, Git, etc.)
- You can optionally start at a different index (other than 0) if you already have locations. For example, you can start at 27 since the original version of the Spyfall Discord bot ends at index 26.

## Optional
- Change the font by replacing font.ttf file with another.
- Increase or decrease size of font by changing "75" in this line: "mf = ImageFont.truetype('font.ttf', 75)."
