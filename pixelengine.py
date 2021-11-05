import pygame
import math
from pathlib import Path
from sys import exit
from __peFont import glyphs

## BASE PROJECT
##--------------
"""
import pixelengine

pe = pixelengine.pixelEngineClass()

while True:
    pe.update()
"""
##--------------

def __clamp(x,minimum,maximum):
    if x < minimum: x = minimum
    elif x > maximum: x = maximum
    return x

def intColor(col):
    binary = bin(col)
    binary = binary.split("0b")
    binary = binary[1]
    if len(binary) < 6:
        for i in range(6-len(binary)):
            binary = "0"+binary
    r = binary[0]+binary[1]
    g = binary[2]+binary[3]
    b = binary[4]+binary[5]

    red = int(r,2)
    green = int(g,2)
    blue = int(b,2)
    
    red = (red/3)*255
    green = (green/3)*255
    blue = (blue/3)*255

    red = round(red)
    green = round(green)
    blue = round(blue)

    red = __clamp(red,0,255)
    green = __clamp(green,0,255)
    blue = __clamp(blue,0,255)

    return (red,green,blue)
def getColorFromTuple(col):
    r = col[0]
    g = col[1]
    b = col[2]

    r = __clamp(r,0,3)
    g = __clamp(g,0,3)
    b = __clamp(b,0,3)

    r = bin(r)
    g = bin(g)
    b = bin(b)

    r = r.split("0b")[1]
    g = g.split("0b")[1]
    b = b.split("0b")[1]

    if len(r) < 2:
        for i in range(2-len(r)):
            r = "0"+r
    if len(g) < 2:
        for i in range(2-len(g)):
            g = "0"+g
    if len(b) < 2:
        for i in range(2-len(b)):
            b = "0"+b

    col = int(r+g+b,2)

    return col
def makeColor(r,g,b):
    x = (r*16)+(g*4)+b
    x = max(0,min(0b111111,x))
    return x

def getSprite(path):
    return Path(path).read_bytes()

PE_BLACK = 0x00
PE_WHITE = 0x3F
PE_RED = makeColor(3,0,0)
PE_ORANGE = makeColor(3,1,0)
PE_YELLOW = makeColor(3,2,0)
PE_GREEN = makeColor(0,2,0)
PE_LIME = makeColor(0,3,0)
PE_BLUE = 0x03
PE_CYAN = makeColor(0,3,3)
PE_AQUA = PE_CYAN
PE_PURPLE = makeColor(1,0,3)
PE_MAGENTA = makeColor(3,0,3)

spriteList = list()

class peSprite():
    def __init__(self,x,y,spritePath,engine):
        self.x = x
        self.y = y
        self.sprite = spritePath
        self.scale = 1
        self.engine = engine
        self.direction = 0
        spriteList.append(self)
    def __exit__(self):
        spriteList.remove(self)
    def update(self):
        pass
    def draw(self):
        self.engine.drawSprite(self.x,self.y,self.sprite,self.direction,self.scale)

class pixelEngineClass():
    def __init__(self,backgroundColor=0x00,screenWidth=256,screenHeight=192,screenMultiplier=3,framesPerSecond=60,title="Pixel Engine v1",icon = pygame.image.load("pixelengine_icon.ico")):
        print("Setup and initialization")
        print(screenWidth)
        print(screenHeight)
        print(screenMultiplier)
        print(backgroundColor)
        print(framesPerSecond)
        print(title)

        self.backgroundColor = backgroundColor
        self.SCREENWIDTH = screenWidth
        self.SCREENHEIGHT = screenHeight
        self.SCREENMULTIPLIER = screenMultiplier
        self.fps = framesPerSecond
        self.timer = 0

        #initialize user input
        self.mouseX = 0
        self.mouseY = 0
        self.inputs = [False]*8
        self.inputsPressed = [0]*8
        self.__mouse = [False]*3
        self.__mousePressed = [0]*3

        pygame.init()
        self.screen = pygame.display.set_mode((self.SCREENWIDTH*self.SCREENMULTIPLIER,self.SCREENHEIGHT*self.SCREENMULTIPLIER))
        self.setIcon(icon)
        self.setTitle(title)
        self.clock = pygame.time.Clock()

        self.screen.fill(intColor(backgroundColor))
        print("Setup complete")
    def update(self):
        #frame start
        for i in range(8):
            self.inputsPressed[i] -= 1
            if self.inputsPressed[i] < 0: self.inputsPressed[i] = 0
        for i in range(3):
            self.__mousePressed[i] -= 1
            if self.__mousePressed[i] < 0: self.__mousePressed[i] = 0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                __id = -1 
                if event.key == pygame.K_UP: #UP
                    __id = 0
                elif event.key == pygame.K_DOWN: #DOWN
                    __id = 1
                elif event.key == pygame.K_LEFT: #LEFT
                    __id = 2
                elif event.key == pygame.K_RIGHT: #RIGHT
                    __id = 3
                elif event.key == pygame.K_z: #A
                    __id = 4
                elif event.key == pygame.K_x: #B
                    __id = 5
                elif event.key == pygame.K_a: #X
                    __id = 6
                elif event.key == pygame.K_s: #Y
                    __id = 7
                if __id != -1:
                    self.inputs[__id] = True
                    if self.inputsPressed[__id] == 0:
                        self.inputsPressed[__id] = 1
            elif event.type == pygame.KEYUP:
                __id = -1 
                if event.key == pygame.K_UP: #UP
                    __id = 0
                elif event.key == pygame.K_DOWN: #DOWN
                    __id = 1
                elif event.key == pygame.K_LEFT: #LEFT
                    __id = 2
                elif event.key == pygame.K_RIGHT: #RIGHT
                    __id = 3
                elif event.key == pygame.K_z: #A
                    __id = 4
                elif event.key == pygame.K_x: #B
                    __id = 5
                elif event.key == pygame.K_a: #X
                    __id = 6
                elif event.key == pygame.K_s: #Y
                    __id = 7
                if __id != -1:
                    self.inputs[__id] = False
                    self.inputsPressed[__id] = 0
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                __id = -1
                if event.button == 1: #LEFT CLICK
                    __id = 0
                elif event.button == 3: #RIGHT CLICK
                    __id = 1
                elif event.button == 2: #MIDDLE CLICK
                    __id = 2
                if __id != -1:
                    self.__mouse[__id] = True
                    if self.__mousePressed[__id] == 0:
                        self.__mousePressed[__id] = 1
            elif event.type == pygame.MOUSEBUTTONUP:
                __id = -1 
                if event.button == 1: #LEFT CLICK
                    __id = 0
                elif event.button == 3: #RIGHT CLICK
                    __id = 1
                elif event.button == 2: #MIDDLE CLICK
                    __id = 2
                if __id != -1:
                    self.__mouse[__id] = False
                    self.__mousePressed[__id] = 0
        __mousePosition = pygame.mouse.get_pos()
        self.mouseX = math.floor(__mousePosition[0]/self.SCREENMULTIPLIER)
        self.mouseY = math.floor(__mousePosition[1]/self.SCREENMULTIPLIER)

        for sprite in spriteList: #update sprites
            sprite.update()
            sprite.draw()
        pygame.display.update()
        self.clock.tick(self.fps)
        #next frame
        self.screen.fill(intColor(self.backgroundColor))
        self.timer += 1
    
    #functions
    #sprites
    def createSprite(self,x,y,spritePath):
        spr = peSprite(x,y,spritePath,self)
        return spr

    #input
    def button(self,btn):
        return self.inputs[btn]
    def buttonPressed(self,btn):
        return self.inputs[btn] and self.inputsPressed[btn] == 1

    def mouse(self,btn):
        return self.__mouse[btn]
    def mousePressed(self,btn):
        return self.__mouse[btn] and self.__mousePressed[btn] == 1

    #draw
    def drawPixel(self,x,y,color,scale=1):
        m = max(1,self.SCREENMULTIPLIER*math.ceil(scale))
        n = self.SCREENMULTIPLIER
        x *= n
        y *= n

        x = math.floor(x/n)*n
        y = math.floor(y/n)*n
        color = intColor(color)
        pygame.draw.rect(self.screen,color,pygame.Rect(x,y,m,m))
    def drawCircle(self,x,y,color,radius,fill=False):
        x = math.floor(x)
        y = math.floor(y)
        inc = 1/math.pi
        radius = abs(radius)
        circumfrence = 2*math.pi*radius
        i = 0
        while i < circumfrence:
            xx = x+(radius*math.cos((i/circumfrence)*(math.pi*2)))
            yy = y+(radius*math.sin((i/circumfrence)*(math.pi*2)))
            self.drawPixel(xx,yy,color,1)
            i += inc
    def drawLine(self,x1,y1,x2,y2,color):
        x1 = math.floor(x1)
        y1 = math.floor(y1)
        x2 = math.floor(x2)
        y2 = math.floor(y2)
        if x1 == x2:
            i = 0
            while i < y2-y1:
                self.drawPixel(x1,y1+i,color,1)
                i += 1
        elif y1 == y2:
            i = 0
            while i < x2-x1:
                self.drawPixel(x1+i,y1,color,1)
                i += 1
        else:
            inc = .25
            direction = math.atan2(y2-y1,x2-x1)
            dist = math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))
            incX = inc*math.cos(direction)
            incY = inc*math.sin(direction)
            x = 0
            y = 0
            i = 0
            self.drawPixel(x1,y1,color,1)
            self.drawPixel(x2,y2,color,1)
            while i < dist:
                x += incX
                y += incY
                self.drawPixel(x1+x,y1+y,color,1)
                i += inc


    def drawRectangle(self,x,y,width,height,color,fill=False):
        self.drawPixel(x,      y,color,1)
        self.drawPixel(x+width,y,color,1)
        self.drawPixel(x,      y+height,color,1)
        self.drawPixel(x+width,y+height,color,1)
        for yy in range(height):
            for xx in range(width):
                if fill:
                    self.drawPixel(x+xx,y+yy,color,1)
                    if xx == width-1:
                        self.drawPixel(x+width,y+yy,color,1)
                    if yy == height-1:
                        self.drawPixel(x+xx,y+height,color,1)
                else:
                    if yy == 0:
                        self.drawPixel(x+xx,y,color,1)
                        if xx == width-2:
                            self.drawPixel(x+width,y+yy,color,1)
                    elif yy == height-1:
                        self.drawPixel(x+xx,y+height,color,1)
                    self.drawPixel(x,y+yy,color,1)
                    self.drawPixel(x+width,y+yy,color,1)
    
    def drawSprite(self,x,y,path,direction=0,scale=1):
        x = math.floor(x)
        y = math.floor(y)
        spr = getSprite(path)
        width = 8
        height = 8
        xoffset = 4
        yoffset = 4
        transparencyColor = 0x00
        i = 0
        initializationDone = False
        data = list()
        for byte in spr:
            if i == 0: width = byte
            elif i == 1: height = byte
            elif i == 2: xoffset = byte
            elif i == 4: yoffset = byte
            elif i == 5:
                transparencyColor = byte
                initializationDone = True
            if initializationDone:
                data.append(byte)
            i += 1
        i = 0
        for byte in data:
            if width != 0 and height != 0:
                xxx = x+((i%width)*scale)-(xoffset*scale)
                yyy = y+(math.floor(i/height)*scale)-(yoffset*scale)
                if byte != transparencyColor:
                    if direction != 0:
                        dirr = math.atan2(xxx-x,yyy-y)
                        dist = math.sqrt(pow(xxx-x,2)+pow(yyy-y,2))
                        dirr += math.radians(direction)
                        xxx = x+(math.sin(dirr)*dist)
                        yyy = y+(math.cos(dirr)*dist)
                        if scale != 1:
                            xxx = math.floor(xxx/scale)*scale
                            yyy = math.floor(yyy/scale)*scale
                    self.drawPixel(xxx,yyy,byte,scale)
            i += 1
    
    def drawGlyph(self,x,y,glyph,color=0x3F): #From https://www.youtube.com/watch?v=FaILnmUYS_U&t=10m51s
        glyphh = glyphs[ord(glyph)]
        for yy in range(8):
            for xx in range(8):
                if glyphh[yy] & (1 << xx):
                    self.drawPixel(x+xx,y+yy,color)

    def drawText(self,x,y,string,color=0x3F):
        i = 0
        for glyph in string:
            self.drawGlyph(x+(i*8),y,glyph,color)
            i += 1
    
    #misc
    def getTitle(self):
        return pygame.display.get_caption()
    def setTitle(self,name):
        pygame.display.set_caption(name)
    
    def setIcon(self,image):
        pygame.display.set_icon(image)