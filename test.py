import pixelengine
import math

pe = pixelengine.pixelEngineClass(pixelengine.makeColor(1,1,1),256,192,3,60)

rainbow = pe.createSprite(128,96,"sprites/rainbow.spr")
cSize = 32
dirr = 0

print(str(pixelengine.getColorFromTuple((1,1,2)))) #should print 22 (0x16) (010110)

def buttonTest():
    if pe.button(0):
        pe.drawPixel(0,0,pixelengine.makeColor(3,1,0),1)
    if pe.button(1):
        pe.drawPixel(1,0,pixelengine.makeColor(3,1,0),1)
    if pe.button(2):
        pe.drawPixel(2,0,pixelengine.makeColor(3,1,0),1)
    if pe.button(3):
        pe.drawPixel(3,0,pixelengine.makeColor(3,1,0),1)
    if pe.button(4):
        pe.drawPixel(4,0,pixelengine.makeColor(3,1,0),1)
    if pe.button(5):
        pe.drawPixel(5,0,pixelengine.makeColor(3,1,0),1)
    if pe.button(6):
        pe.drawPixel(6,0,pixelengine.makeColor(3,1,0),1)
    if pe.button(7):
        pe.drawPixel(7,0,pixelengine.makeColor(3,1,0),1)
        
    if pe.buttonPressed(0):
        pe.drawPixel(0,1,pixelengine.makeColor(3,1,0),1)
    if pe.buttonPressed(1):
        pe.drawPixel(1,1,pixelengine.makeColor(3,1,0),1)
    if pe.buttonPressed(2):
        pe.drawPixel(2,1,pixelengine.makeColor(3,1,0),1)
    if pe.buttonPressed(3):
        pe.drawPixel(3,1,pixelengine.makeColor(3,1,0),1)
    if pe.buttonPressed(4):
        pe.drawPixel(4,1,pixelengine.makeColor(3,1,0),1)
    if pe.buttonPressed(5):
        pe.drawPixel(5,1,pixelengine.makeColor(3,1,0),1)
    if pe.buttonPressed(6):
        pe.drawPixel(6,1,pixelengine.makeColor(3,1,0),1)
    if pe.buttonPressed(7):
        pe.drawPixel(7,1,pixelengine.makeColor(3,1,0),1)

while True:
    buttonTest()

    cSize = 32+(math.sin(pe.timer/30))*8

    rainbow.direction = dirr
    dirr += 1
    if dirr > 359: dirr = 0
    #rainbow.scale = 2+(math.sin(pe.timer/15))
    #pe.drawRectangle(5,5,16,16,pixelengine.makeColor(1,2,3),True)
    #pe.drawPixel(5,   5   ,pixelengine.PE_RED,1)
    #pe.drawPixel(5+16,5   ,pixelengine.PE_RED,1)
    #pe.drawPixel(5,   5+16,pixelengine.PE_RED,1)
    #pe.drawPixel(5+16,5+16,pixelengine.PE_RED,1)
    #pe.drawLine(128,96,128+(math.cos(pe.timer/30)*cSize),96+(math.sin(pe.timer/30)*cSize),pixelengine.makeColor(0,3,0))
    #pe.drawCircle(128,96,pixelengine.makeColor(0,3,0),cSize,False)
    pe.update()