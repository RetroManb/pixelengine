import pixelengine
from math import floor

STATE_DRAWING = 0
STATE_MENU = 1

MAXMENU = 2

global cursorX
global cursorY
global spriteData
global sprite
global scale
global chosenColor
global cursorOutside
cursorX = 0
cursorY = 0
spriteData = {
    "width": 8,
    "height": 8,
    "xOffset": 4,
    "yOffset": 4,
    "transparentColor": 0x00
}
sprite = [0x00]*(spriteData["width"]*spriteData["height"])
scale = 2
chosenColor = (3,0,0)
cursorOutside = False
def newSprite(width,height):
    global cursorX
    global cursorY
    global spriteData
    global sprite
    global scale
    if width < 1:
        width = 1
    elif width > 255:
        width = 255
    
    if height < 1:
        height = 1
    elif height > 255:
        height = 255

    cursorX = 0
    cursorY = 0
    spriteData = {
        "width": width,
        "height": height,
        "xOffset": 4,
        "yOffset": 4,
        "transparentColor": 0x00
    }
    sprite = [0x00]*(spriteData["width"]*spriteData["height"])

pe = pixelengine.pixelEngineClass(0x00,256,192,3,60,"Pixel Engine v1 - Sprite editor")

def update():
    global cursorX
    global cursorY
    global spriteData
    global sprite
    global chosenColor
    global scale
    global cursorOutside
    #cursor
    cursorX = floor((pe.mouseX/2)-(64-(spriteData["xOffset"])))
    cursorY = floor((pe.mouseY/2)-(48-(spriteData["yOffset"])))

    if cursorX < 0:
        cursorX = 0
        cursorOutside = True
    elif cursorX > spriteData["width"]-1:
        cursorX = spriteData["width"]-1
        cursorOutside = True
    if cursorY < 0:
        cursorY = 0
        cursorOutside = True
    elif cursorY > spriteData["height"]-1:
        cursorY = spriteData["height"]-1
        cursorOutside = True
    else:
        if cursorOutside:
            cursorOutside = False

    #placing color
    if pe.mouse(0) and not cursorOutside:
        sprite[(cursorY*spriteData["height"])+cursorX] = pixelengine.makeColor(chosenColor[0],chosenColor[1],chosenColor[2])
        
    #erasing color
    if pe.mouse(1) and not cursorOutside:
        sprite[(cursorY*spriteData["height"])+cursorX] = spriteData["transparentColor"]
        

def draw():
    global cursorX
    global cursorY
    global spriteData
    global sprite
    global scale
    global chosenColor

    #RGB selector
    pe.drawRectangle(0,0,9,9,0x3F,False)
    pe.drawRectangle(1,1,7,7,pixelengine.makeColor(2,2,2),True)
    for i in range(3):
        for j in range(4):
            #c = pixelengine.makeColor(j*int(i==0),j*int(i==1),j*int(i==2)),
            if i == 0:
                c = pixelengine.makeColor(j,chosenColor[1],chosenColor[2])
            elif i == 1:
                c = pixelengine.makeColor(chosenColor[0],j,chosenColor[2])
            elif i == 2:
                c = pixelengine.makeColor(chosenColor[0],chosenColor[1],j)
            pe.drawRectangle(1+(j*4),1+(i*3),4,3,c,True)
    pe.drawRectangle(0,9,9,3,0x3F,False)
    pe.drawRectangle(1,10,7,1,pixelengine.makeColor(chosenColor[0],chosenColor[1],chosenColor[2]),False)

    #draw sprite
    pe.drawRectangle(127+((-spriteData["xOffset"])*scale),95+((-spriteData["yOffset"])*scale),(spriteData["width"]*2)+1,(spriteData["height"]*2)+1,0x3F,False)
    for yy in range(spriteData["height"]):
        for xx in range(spriteData["width"]):
            x = 128+((xx-spriteData["xOffset"])*scale)
            y = 96+((yy-spriteData["yOffset"])*scale)
            color = sprite[(yy*spriteData["height"])+xx]
            pe.drawPixel(x,y,color,2)

    #draw cursor
    x = 128+((-spriteData["xOffset"])*scale)+(cursorX*scale)
    y = 96+((-spriteData["yOffset"])*scale)+(cursorY*scale)
    pe.drawRectangle(pe.mouseX-1,pe.mouseY-1,2,2,pixelengine.makeColor(1,1,1),False)
    pe.drawPixel(pe.mouseX,pe.mouseY,pixelengine.makeColor(chosenColor[0],chosenColor[1],chosenColor[2]),1)

while True:
    update()
    draw()
    pe.update()