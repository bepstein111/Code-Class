from Ball import Ball

def setup():
    global ball1
    global ball2
    size(400,400)
    ball1 =  Ball(54,'#FF0000')
    ball2 =  Ball(20,'#00FF00')
    print ball1,ball2

def draw():
    background(0)
    global ball1,ball2
    ball1.move()
    ball2.move()
    if (ball1.intersect(ball2)):
        text('bump',10,390)
        ball1.highlight()
        ball2.highlight()
    else:
        text('free',10,390)
