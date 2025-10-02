import pygameforbabies as pfb
pfb.window.resizeable = True
pfb.window.title = "Debug Window"

floor = pfb.StaticBody([0, pfb.window.size[1] - 50], [pfb.window.size[0], 50], color="red")
floor.add()
mrow = pfb.RigidBody([100,100], color="blue")
mrow.add()
pfb.mainloop()