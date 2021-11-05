import pixelengine
import math

pe = pixelengine.pixelEngineClass(0x00,320,256,3,60,"Planet gravity test")

G = 6.67408*pow(10,-2)

ball = {
    "x": 0,
    "y": 0,
    "xsp": 0,
    "ysp": 0,
    "radius": 8,
    "mass": 10
}
planet = {
    "x": 160,
    "y": 128,
    "radius": 64,
    "mass": 100
}

def getDist():
    return math.sqrt(pow(planet["x"]-ball["x"],2)-pow(planet["y"]-ball["y"],2))
def distCheck():
    return (planet["radius"]+ball["radius"])/2

def update():
    direction = math.atan2(planet["y"]-ball["y"],planet["x"]-ball["x"])
    dist = math.sqrt(pow(planet["x"]-ball["x"],2)-pow(planet["y"]-ball["y"],2))
    force = G*((ball["mass"]*planet["mass"])/pow(dist,2))

    ball["xsp"] += math.cos(direction)*force
    ball["ysp"] += math.sin(direction)*force
    ball["x"] += ball["xsp"]
    ball["y"] += ball["ysp"]

    dist = getDist()
    if dist < distCheck():
        direction = math.atan2(planet["y"]-ball["y"],planet["x"]-ball["x"])
        prevX = ball["x"]
        prevY = ball["y"]
        while dist < distCheck():
            ball["x"] -= math.cos(direction)
            ball["y"] -= math.sin(direction)
            dist = getDist()
        ball["xsp"] *= -1
        ball["ysp"] *= -1

    if pe.mousePressed(0):
        direction = math.atan2(pe.mouseY-ball["y"],pe.mouseX-ball["x"])
        ball["xsp"] += math.cos(direction)*2
        ball["ysp"] += math.sin(direction)*2


def draw():
    pe.drawCircle(planet["x"],planet["y"],pixelengine.PE_GREEN,planet["radius"],False)
    pe.drawCircle(ball["x"],ball["y"],0x3F,ball["radius"],False)

while True:
    update()
    draw()
    pe.update()