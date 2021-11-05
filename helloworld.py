from math import cos, sin
import pixelengine

pe = pixelengine.pixelEngineClass()
pe.setTitle("Hello world!")

txt = ["H","E","L","L","O"," ","W","O","R","L","D","!"]

while True:
    for i in range(len(txt)):
        scale = 4
        iScale = 16
        x = 80+(i*8)+(cos(((i*iScale)+pe.timer)/30)*scale)
        y = 88+(sin(((i*iScale)+pe.timer)/30)*scale)
        pe.drawGlyph(x+1,y+1,txt[i],pixelengine.makeColor(1,1,3))
        pe.drawGlyph(x,y,txt[i])
    pe.update()