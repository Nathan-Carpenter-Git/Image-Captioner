# Creates caption onto image with locations (locations must be labled via numbers in order with conjuction with locations)
# Example: 0.png, 1.png | locations = {"Airport Terminal", "Avengers Movie"} - 0.png will be captioned with Airport Terminal while 1.png will be captioned with Avengers Movie
from PIL import Image, ImageFont, ImageDraw

# Draws on image, creating a caption based on image sizing
def DrawOnImage(text, imageNumber, captionedNumber):
    try:
        I = Image.open(f"{imageNumber}.png")
    except:
        print(f"Couldn't open {imageNumber}.png")
        return
    
    width, height = I.size

    Im = ImageDraw.Draw(I)
    mf = ImageFont.truetype('font.ttf', 75)

    Im.text((width/2, height/2), text, fill=(0, 0, 0), font=mf, anchor="mm")

    I.save("{number}_Captioned.png")
    print(f"Saved {captionedNumber}_Captioned.png successfully with {text}")

# Enter locations you want to caption here
locations = ["Airport Terminal", "Avengers Movie", "Bioweapons Lab", "Bowling Alley", "Cafeteria", "City Park", "Concert Venue", "Corporate Office", "Gameshow", "Gym", "High-Stakes Poker Game", "Hogwarts Castle", "Hospital Waiting Room", "International Harbor", "Laboratory", "MI-6", "Movie Theater", "Mountain Cabin", "Polling Place", "Soap Opera", "Spy Convention", "Street Market", "Thrift Shop", "Wild West Town", "YouTuber Mansion", "Zoo", "Campsite"]

# Captures starting number for captioning (Helps in situations where you already have locations in another folder)
while(True):
    try:
        startingNumber = int(input("Enter caption starting number: "))
        break

    except:
        print("Input invalid")

# Main captioning loop
for i in range(len(locations)):
    DrawOnImage(locations[i], i, i + startingNumber)