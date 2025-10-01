import pygame
import pygameforbabies as pfb
pfb.window.resizeable = True
debugbut = pfb.Button(camaffect=True)
debugbut.add()
debugslider = pfb.Slider([0,100],camaffect=True)
debugslider.add()
debugslider = pfb.Slider([0,100],camaffect=False)
debugslider.add()
def wasd(keys):
    if keys[pygame.K_w]:
        pfb.camerapos[1] -= 10
    if keys[pygame.K_s]:
        pfb.camerapos[1] += 10
    if keys[pygame.K_a]:
        pfb.camerapos[0] -= 10
    if keys[pygame.K_d]:
        pfb.camerapos[0] += 10
def _meow2(scroll):
    pfb.camerazoom -= (scroll[1] * 0.1)
pfb.connect.onmousescroll = _meow2
pfb.connect.onkeydown = wasd
pfb.mainloop()