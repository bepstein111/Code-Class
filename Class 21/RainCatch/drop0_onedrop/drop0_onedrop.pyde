#from Drop import Drop
def setup():
    global x,y
    size(400,400)
    background(0)
    x = width/2
    y = 0

def draw():
    global x,y
    background(255)
    fill(50,100,150)
    noStroke()
    ellipse(x,y,16,16)  #'raindrop'
    y=y+1  #move down