import pygameforbabies as pfb
pfb.window.resizeable = True
pfb.window.title = "Debug Window"
char = pfb.Character([100, 0])
char.add()
char.shape.friction = 0.5  # or even 0 for very slippery movement
lo = pfb.keys.InputMap([pfb.keys.A, pfb.keys.LEFT])
lol = pfb.keys.InputMap([pfb.keys.D, pfb.keys.RIGHT])
pfb.physics_size = [10000,10000]
def keydown(keys):
    baby.pos = pfb.subiter(char.get_position(), [25,40])
    baby.rotation = -char.get_angle()
    pfb.camerapos = pfb.subiter(char.get_position(), [400,300])
    if keys[pfb.keys.A]:
        char.move_left()
    if keys[pfb.keys.D]:
        char.move_right()
    #print(pfb.keys.get_axis(keys, lo, lol))
def keypressed(key):
    if key == pfb.keys.SPACE:
        char.jump(400)
fsp = pfb.Sprite("assets/exec.png", [0,525], [10000, 50])
fsp.add()
baby = pfb.Sprite("baby.jpeg", scale=[50,80])
baby.add()
baby.removecolor = baby.image.get_at([10,10]) # type: ignore
pfb.connect.onkeydown = keydown
pfb.connect.onkeypress = keypressed
floor = pfb.StaticBody([0, 550], [10000,50], color="red")
floor.add()
mrow = pfb.RigidCircle([100,100], 100)
mrow.add()
wall = pfb.StaticCircle([90,130], 50)
wall.add()
pfb.mainloop()