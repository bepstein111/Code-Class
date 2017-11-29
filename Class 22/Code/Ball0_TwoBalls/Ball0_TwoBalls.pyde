from Ball import Ball

#Simplify the problem to 2 bals moving
def setup():
    global ball1
    global ball2
    size(400,400)
    ball1 =  Ball(54,'#FF0000')
    ball2 =  Ball(20,'#00FF00')
    print ball1,ball2

def draw():
    global ball1,ball2
    background(255)
    ball1.move()
    ball2.move()
    