class Catcher():
    r = 0
    x = 0
    y = 0 
    col = color(50,10,10,150)
    
    def __init__(this,radius):
        global x,y,r, col
        this.r = radius
        this.x = 0
        this.y = 0
        col = color(50,10,10,150)
    
    def setLocation(this,tempX, tempY):
        global x,y
        this.x = tempX
        this.y = tempY
        
    def display(this):
        global x,y
        global r
        stroke(0)
        fill(col)
        d = this.r * 2
        ellipse(this.x,this.y,d,d)
        
    def intersect(self, other):
        distance = dist(self.x, self.y,other.x, other.y)
        if (distance < self.r + other.r):
            return True
        else:
            return False
        