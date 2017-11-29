from Drop import Drop
global drop
def setup():
    global x,y, drop
    size(400,400)
    background(0)
    drop = Drop()


def draw():
    global x,y,drop
    background(0)
    drop.move() #move down
    drop.display()