class Catcher():
    def __init__(this,radius):
        global x,y,r
        r = radius
        x = 0
        y = 0 
    
    def setLocation(this,tempX, tempY):
        global x,y
        x = tempX
        y = tempY
        
    def display(this):
        global x,y
        global r
        stroke(0)
        fill(175)
        d = r * 2
        ellipse(x,y,d,d)