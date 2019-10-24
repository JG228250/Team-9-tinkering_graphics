import pygame
import os


pygame.init()

display = pygame.display.set_mode((800, 600))

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

origFilename = 'test image'
origImgPath = os.path.join('Contract4Images', origFilename + '.jpg')
origImg = pygame.image.load(origImgPath).convert()

imgWidth = origImg.get_width()
imgHeight = origImg.get_height()

greenImg = pygame.Surface((imgWidth, imgHeight))
blueImg = pygame.Surface((imgWidth, imgHeight))
yellowImg = pygame.Surface((imgWidth, imgHeight))

for i in range(imgWidth):
    for p in range(imgHeight):
        for j in range(3):
            pixelColour = origImg.get_at((i, p))
            if j != 2:
                colourHolder = pixelColour[0]
                pixelColour[0] = pixelColour[j + 1]
                pixelColour[j + 1] = colourHolder
                if j == 0:
                    greenImg.set_at((i, p), pixelColour)
                else:
                    blueImg.set_at((i, p), pixelColour)
            else:
                pixelColour[1] = pixelColour[0]
                yellowImg.set_at((i, p), pixelColour)

greenFilename = os.path.join('Contract4Images', origFilename + ' (Green)' + '.png')
pygame.image.save(greenImg, greenFilename)

blueFilename = os.path.join('Contract4Images', origFilename + ' (Blue)' + '.png')
pygame.image.save(blueImg, blueFilename)

yellowFilename = os.path.join('Contract4Images', origFilename + ' (Yellow)' + '.png')
pygame.image.save(yellowImg, yellowFilename)
