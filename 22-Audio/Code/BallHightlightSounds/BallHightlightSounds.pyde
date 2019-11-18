from Ball import Ball
add_library('sound')
blip = None

def setup():
    global ball1, ball2, blip
    size(400,400)
    ball1 =  Ball(54,'#FF0000')
    ball2 =  Ball(20,'#00FF00')
    blip = SoundFile(this,'blip.wav')
    print blip.frames()
def draw():
    background(255)
    global ball1,ball2, blip
    ball1.move()
    ball2.move()
    if (ball1.intersect(ball2) or ball2.intersect(ball1)):
        blip.play()
        ball1.highlight()
        ball2.highlight()
        text('bump',10,390)
    else:
        text('free',10,390)
    ball1.display()
    ball2.display()