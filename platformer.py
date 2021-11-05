import pixelengine

pe = pixelengine.pixelEngineClass(0,320,240,3,60,"Test Platformer")

screen = [
    {
        "....................",
        "....................",
        "....................",
        "....................",
        "....................",
        "....................",
        "....................",
        "....................",
        "....................",
        "....................",
        "....................",
        "....................",
        "....................",
        "####################",
        "####################",
    },
    {
        "....................",
        "....................",
        "....................",
        "....................",
        "....................",
        "....................",
        "....................",
        "....................",
        "..................#.",
        "..............#...#.",
        "..........#...#...#.",
        "......#...#...#...#.",
        "..#...#.............",
        "####################",
        "####################",
    },
]

level = {
    0,1,0
}

camX = 0

class Player(pixelengine.peSprite):
    def __init__(self,x,y,engine):
        pixelengine.peSprite.__init__(self,x,y,"sprites/platformer_player.spr",engine)
        self.sprite = "sprites/platformer_player.spr"
        self.xsp = 0
        self.ysp = 0
        self.width = 16
        self.height = 16
    def update(self):
        self.x += self.xsp
        self.ysp += .125
        self.y += self.ysp
    def draw(self):
        self.engine.drawSprite(self.x-camX,self.y,self.sprite,self.direction,self.scale)

player = Player(16,16,pe)

def drawLevel():
    pass

while True:
    pe.update()
    drawLevel()