add_library('video')
#Angela Chang 11/28/2017 for Emerson IN334
#grab video and overlay buttons that open links on top
#click on the image changes button color to the pixel
trackColor = "#9AA121"
lastTime = 0

def setup():
    global video, trackColor
    size(640,480)
    frameRate(30)
    video = Capture(this,640,480,30)
    video.start()
    
def draw():
    global video, trackColor, lastTime
    fill(trackColor)
    if (video.available()):
        video.read()
    set(0,0, video)
    #before searching, get "closest" color 
    #easy for first pixel to beat
    worldRecord = 500
    closestX = 0  #X coordinate of closest color
    closestY = 0  #Y coordinate of closest color
    
    #loop through every pixel
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
    #tracking needs to be.
    if worldRecord < 10:
        fill(trackColor)
        strokeWeight(4.0)
        stroke(0)
        #draw a marker on the tracked pixel
        ellipse(closestX,closestY, 16,16)
 
    if closestY<30: #are we in upper quadrant
        elapsed = millis() - lastTime
        #at least 10 seconds since last link
        if elapsed>10000: 
            print elapsed, millis(),lastTime
            if closestX<100:
                link('http://emerson.edu')
                lastTime = millis()
            elif closestX>=110 and closestX<210:
                link('http://google.com')
                lastTime = millis()
            elif closestX>220:
                link('http://bing.com')
                lastTime = millis()

    rect(0,0,100,30)
    rect(110,0,100,30)
    rect(220,0,100,30)
    fill(0)
    text("Emerson",10,20)
    text("google",120,20)
    text("bing",230,20)
        
def mousePressed():
    global trackColor
    #Save color where the mouse is clicked in trackColor variable
    loc = mouseX + mouseY*video.width
    trackColor = video.pixels[loc]
    #print(hex(trackColor,6))


        