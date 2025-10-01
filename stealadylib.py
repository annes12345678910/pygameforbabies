import pygameforbabies as pfb
title = pfb.Text("STEAL A DYLIB", [100,100], 100)
title.add()
pfb.window.changeicon("assets/exec.png")
play = pfb.Button(pos=[300,200], text="Play", onclick=lambda: setattr(pfb, 'scene', "steal"))
play.add()
pfb.mainloop()