add_library('sound')
blip = None
radius = 120
x = 0
speed = 3.0
direction = 1
def setup():
    global blip, x
    size(800, 440)
    ellipseMode(RADIUS)
    blip = SoundFile(this, 'blip.wav')
    x = width/2 #start in the center
def draw():
    global x, direction
    background(0)
    x += speed * direction
    if x > width-radius or x < radius:
        direction = -direction #flip direction
        blip.play()
    if direction == 1:
        arc(x, 220, radius, radius, 0.52, 5.76) #Face right
    else:
        arc(x, 220, radius, radius, 3.67, 8.9) #face left
#https://processing.org/reference/libraries/sound/index.html
#https://processing.org/reference/libraries/sound/SoundFile.html