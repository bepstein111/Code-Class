#http://py.processing.org/reference/dist.html
#if the distance is less than the sum of the radii, they intersect
distance = 0.0
def setup():
    frameRate(30)
    global x1,y1,r1,r2
    size(400,200)
    noStroke()
    x1 = 199  #first ball at 45,100
    y1 = 100 
    r1 = 25  #radius for two balls equal
    r2 = 25

def draw():
    background(0)
    global x1,y1,x2,y2,r1,r2
    ball1 = ellipse(x1,y1,r1*2,r1*2)
    ball2 = ellipse(mouseX,mouseY,r2*2,r2*2)
    string3 = 'Touching? '+str(intersect(x1,y1,mouseX,mouseY,r1,r2))
    string1 = str(round(distance,2)) + ' <= '+str(r1)+' + '+ str(r2)
    string2 = 'mouse: '+str(mouseX)+', '+ str(mouseY)
    text(string1,5, 150)
    text(string2,5, 170)
    text(string3,5, 190)
    
def intersect(p1x,p1y,p2x,p2y,ra1,ra2):
    global distance
    distance = dist(p1x,p1y,p2x,p2y)
    if (distance < ra1+ra2):
        return True
    else:
        return False