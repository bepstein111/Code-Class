add_library('video')
#Click the mouse to set the color to track
trackColor = None

def setup():
    global video, trackColor
    size(320,240)
    video = Capture(this,320,240,30)
    video.start()
    #start tracking red
    trackColor = color(255,0,0)
    
def draw():
    global video, trackColor
    if (video.available()):
        video.read()
    set(0,0, video)
    
    worldRecord = 500
    closestX = 0
    closestY = 0
    
    for x in range(video.width-1):
        for y in range(video.height-1):
            loc = x + y * (video.width)
            
            #what's the currentcolor
            currentColor = video.pixels[loc]
            r1 = red(currentColor)
            g1 = green(currentColor)
            b1 = blue(currentColor)
            r2 = red(trackColor)
            g2 = green(trackColor)
            b2 = blue(trackColor)
            #use euclidean distance to compare colors
            d = dist(r1,g1,b1,r2,g2,b2)
            if  d < worldRecord:
                worldRecord = d
                closestX = x
                closestY = y
    #We only consider the color found if its color 
    #distance is less than 10. 
    #This threshold of 10 is arbitrary and you can 
    #adjust this number depending on how accurate 
    #you require the tracking to be.
    if worldRecord < 10:
        fill(trackColor)
        strokeWeight(4.0)
        stroke(0)
        ellipse(closestX,closestY, 16,16)
        
def mousePressed():
    global trackColor
    #Save color where the mouse is clicked in trackColor variable
    loc = mouseX + mouseY*video.width
    trackColor = video.pixels[loc]
    print(hex(trackColor,6))