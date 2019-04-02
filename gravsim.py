import gravity
from PIL import Image, ImageDraw

masses = [gravity.Mass(2000000, (320, 200, 0), v0=(60, 0, 0)), gravity.Mass(2000000, (320, 400, 0), v0=(-60, 0, 0)), 
                gravity.Mass(20000, (320, 160, 0), v0=(-140, 0, 0)), gravity.Mass(20000, (320, 440, 0), v0=(140, 0, 0))]
dt = 0.1
t = 10
frames = []

for i in range(0, int(t/(dt/1000))):
    if(i%int(50/dt) == 0):
        image = Image.new('L', (640, 480))
        img = ImageDraw.Draw(image)
    
        for mass in masses:
            img.ellipse((mass.pos[0]-2, mass.pos[1]-2, mass.pos[0]+2, mass.pos[1]+2), fill=(255))
    
        frames.append(image)
    
    gravity.update(masses, dt)

frames[0].save('electro.gif', format='GIF', append_images=frames[1:], save_all=True, duration=50, loop=0)
