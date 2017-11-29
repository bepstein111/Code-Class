class Catcher():
    r = 0
    x = 0
    y = 0 
    def __init__(this,radius):
        global x,y,r
        this.r = radius
        this.x = 0
        this.y = 0
    
    def setLocation(this,tempX, tempY):
        global x,y
        x = tempX
        y = tempY
        
    def display(this):
        global x,y
        global r
        stroke(0)
        fill(175)
        d = this.r * 2
        ellipse(x,y,d,d)