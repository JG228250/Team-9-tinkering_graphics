import pygame
import os

pygame.init()

colCheck = int(input("What colour would you like to change from?\n1. Red\n2. Green\n\nPlease "
                     "enter a number: "))

display = pygame.display.set_mode((800, 600))

red = (255, 0, 0)  # setting colour values to variables
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

origFilename = 'test image'
origImgPath = os.path.join('Contract4Images/ImageChange', origFilename + '.jpg')
origImg = pygame.image.load(origImgPath).convert()  # loading image

imgWidth = origImg.get_width()  # getting height and width of test image
imgHeight = origImg.get_height()

greenImg = pygame.Surface((imgWidth, imgHeight))  # setting new images to same surface
blueImg = pygame.Surface((imgWidth, imgHeight))
yellowImg = pygame.Surface((imgWidth, imgHeight))
redImg = pygame.Surface((imgWidth, imgHeight))

if colCheck == 1:
    for i in range(imgWidth):
        for p in range(imgHeight):
            for j in range(3):
                pixelColour = origImg.get_at((i, p))  # get_at gets the colour of the pixels
                if j != 2:
                    tempCol = pixelColour[0]
                    pixelColour[0] = pixelColour[j + 1]
                    pixelColour[j + 1] = tempCol
                    if j == 0:
                        greenImg.set_at((i, p), pixelColour)  # set_at changes the pixel colour
                    else:
                        blueImg.set_at((i, p), pixelColour)
                else:
                    pixelColour[1] = pixelColour[0]
                    yellowImg.set_at((i, p), pixelColour)

    blueFilename = os.path.join('Contract4Images', origFilename + ' (Blue)' + '.png')
    pygame.image.save(blueImg, blueFilename)

    yellowFilename = os.path.join('Contract4Images', origFilename + ' (Yellow)' + '.png')
    pygame.image.save(yellowImg, yellowFilename)

    greenFilename = os.path.join('Contract4Images', origFilename + ' (Green)' + '.jpg')
    pygame.image.save(greenImg, greenFilename)

elif colCheck == 2:
    for i in range(imgWidth):
        for p in range(imgHeight):
            for j in range(3):
                pixelColour = origImg.get_at((i, p))  # get_at gets the colour of the pixels
                if j != 2:
                    tempCol = pixelColour[0]
                    pixelColour[0] = pixelColour[j + 1]
                    pixelColour[j + 1] = tempCol
                    if j == 0:
                        redImg.set_at((i, p), pixelColour)  # set_at changes the pixel colour
                    elif j != 0:
                        pixelColour[2] = pixelColour[1]
                        blueImg.set_at((i, p), pixelColour)
                else:
                    pixelColour[0] = pixelColour[1]
                    yellowImg.set_at((i, p), pixelColour)

    blueFilename = os.path.join('Contract4Images', origFilename + ' (Blue)' + '.png')
    pygame.image.save(blueImg, blueFilename)

    yellowFilename = os.path.join('Contract4Images', origFilename + ' (Yellow)' + '.png')
    pygame.image.save(yellowImg, yellowFilename)

    redFilename = os.path.join('Contract4Images', origFilename + ' (Red)' + '.png')
    pygame.image.save(redImg, redFilename)
