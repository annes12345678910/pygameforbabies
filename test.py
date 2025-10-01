import pygameforbabies as pfb
import random
pfb.window.changeicon("assets/fish.png")
pfb.window.title = "fish game"
pfb.window.screencolor = "blue"
eat = pfb.Sound("assets/eat.mp3")
fish = pfb.Sprite("assets/fish.png")
fish.add()
fish.pos[1] = 536
def mousemove(pos):
    fish.pos[0] = pos[0] - 32
planks = []
oils = []
score = 0
st = pfb.Text(f"Score: 0", size=50)
st.add()
def update():
    global score
    if random.randint(1,10) == 1:
        plank = pfb.Sprite("assets/plankton.png", [random.randint(0, 800), 0])
        plank.add()
        planks.append(plank)
    if random.randint(1,30) == 1:
        oil = pfb.Sprite("assets/oil.png", [random.randint(0, 800), 0])
        oil.add()
        oils.append(oil)
    for i in planks:
        i.move(0,10)
        if i.iscolliding(fish):
            i.pos = [-100,0]
            eat.play()
            score += 1
    for i in oils:
        i.move(0,10)
        if i.iscolliding(fish):
            with open("score.txt", "a") as f:
                f.write(str(score) + "\n")
            print(score)
            pfb.quit_app()
            
    st.text = f"Score: {score}"
        
pfb.connect.onmousemove = mousemove
pfb.connect.onupdate = update
pfb.mainloop()