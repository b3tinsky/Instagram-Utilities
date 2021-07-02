import shutil, os, re
import backopyConfig
from sys import exit
from instabot import Bot
from pathlib import Path
from PIL import Image, ImageFilter
from numpy import add, random
import operator

# Removes token so next time login is fluent
# shutil.rmtree('C:\\Users\\B3TINSKY\\Documents\\Code\\Instagram Utilities\\config')

user_name = backopyConfig.USERNAME
password = backopyConfig.PASSWORD

CBnewAddress = 'C:\\Users\\B3TINSKY\\Pictures\\Backopy Memes\\Testing\\New\\CB'
BBnewAddress = 'C:\\Users\\B3TINSKY\\Pictures\\Backopy Memes\\Testing\\New\\BB'
WBnewAddress = 'C:\\Users\\B3TINSKY\\Pictures\\Backopy Memes\\Testing\\New\\WB'
memeArchive = 'C:\\Users\\B3TINSKY\\Pictures\\Backopy Memes\\Testing\\Old'

memeFoldersWithMemes = []

def resize(ImageFilePath, backgroundType):

    image = Image.open(ImageFilePath, 'r')
    image_size = image.size
    width = image_size[0]
    height = image_size[1]

    if(width != height):
        bigside = width if width > height else height
        
        if(backgroundType == 0) :
            # Loop through every pixel in the image and modify it
            original_color_count = {}
            for w in range(width):
                for h in range(height):
                    current_color = image.getpixel((w, h))

                    if current_color in original_color_count:
                        original_color_count[current_color] += 1
                    else:
                        original_color_count[current_color] = 1

            max_color = max(original_color_count.items(), key=operator.itemgetter(1))[0]
            # Fill with blurred image
            # background = Image.open(ImageFilePath, 'r').resize((bigside, bigside), 2).filter(ImageFilter.GaussianBlur(9))
            background = Image.new('RGB', (bigside, bigside), max_color)

            

        # elif (backgroundType == 1) :
        #     # Fill with solid color (white)
        #     background = Image.new('RGB', (bigside, bigside), (255, 255, 255))
        # else :
        #     # Fill with solid color (black)
        #     background = Image.new('RGB', (bigside, bigside), (0, 0, 0))

        # Decide size of bars on larger side
        offset = (int(round(((bigside - width) / 2), 0)), int(round(((bigside - height) / 2),0)))

        # Set original image on top of decided background
        background.paste(image, offset)
        background.save(ImageFilePath)
        
        # Let's be tidy
        print("Image has been resized !")
        image.close()
        background.close()

    else:
        print("Image is already a square, it has not been resized !")

def uploadMeme(address):
    # Wake up bot :)
    # bot = Bot()
    # bot.login(username = backopyConfig.USERNAME, password = backopyConfig.PASSWORD)

    memeFolder = os.listdir(address)
    backgroundType = 0
    if(address == WBnewAddress) :
        backgroundType = 1
    elif (address == BBnewAddress) :
        backgroundType = 2

    random.shuffle(memeFolder)

    memeName = memeFolder[0]

    beforePost = address + '\\' + memeName
    afterPost = memeArchive + '\\' + memeName
    # shutil.copy(beforePost, afterPost)
    resize(beforePost, backgroundType)
    # bot.upload_photo(beforePost, caption="")
    # os.remove(beforePost + '.REMOVE_ME')
    # bot.logout()


if len(os.listdir(CBnewAddress)) != 0:
    memeFoldersWithMemes.append(CBnewAddress)
if len(os.listdir(BBnewAddress)) != 0:
    memeFoldersWithMemes.append(BBnewAddress)
if len(os.listdir(WBnewAddress)) != 0:
    memeFoldersWithMemes.append(WBnewAddress)

# No Memes Available -> Why bother with continuing
if(len(memeFoldersWithMemes) == 0) :
    exit()

memeChoice = random.randint(0, len(memeFoldersWithMemes))

uploadMeme(memeFoldersWithMemes[memeChoice])