import pygameforbabies as pfb
import random
pfb.window.title = "paint"
pfb.window.resizeable = True
clr = "red"
pfb.Text("press g to screenshot and c to change color", [0,0], 50, "white",False).add()
pfb.changemusic("sample.mp3")
def _meow(k):
        if k == pfb.keys.W:
            pfb.camerapos[1] -= 3
        if k == pfb.keys.A:
            pfb.camerapos[0] -= 3
        if k == pfb.keys.S:
            pfb.camerapos[1] += 3
        if k == pfb.keys.D:
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