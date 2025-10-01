import pygameforbabies as pfb
from pygameforbabies import keys
import random
pfb.window.title = "paint"
pfb.window.resizeable = True
clr = "red"
pfb.Text("press g to screenshot and c to change color", [0,0], 50, "white",False).add()
pfb.changemusic("assets/sample.mp3")
def _meow(k):
        if k[keys.W]:
            pfb.camerapos[1] -= 3
        if k[keys.A]:
            pfb.camerapos[0] -= 3
        if k[keys.S]:
            pfb.camerapos[1] += 3
        if k[keys.D]:
            pfb.camerapos[0] += 3
pfb.connect.onkeydown = _meow
def mm(pos):
    pfb.Circle(pos,clr).add()
def keypress(key):
    global clr
    #print(key)
    if key == pfb.keys.G:
        pfb.screenshot("drawing.png")
    if key == pfb.keys.C:
        clr = random.choice(["red", "blue", "yellow","green","white"])
pfb.connect.onmousedown = mm
pfb.connect.onkeypress = keypress
pfb.mainloop()