import pygameforbabies as pfb
pfb.window.resizeable = True
pfb.window.title = "Debug Window"

floor = pfb.StaticBody([0, pfb.window.size[1] - 50], [pfb.window.size[0], 50], color="red")
floor.add()
mrow = pfb.RigidCircle([100,100], 20)
mrow.add()
wall = pfb.StaticCircle([90,130], 10)
wall.add()
pfb.mainloop()