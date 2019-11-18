add_library('video')
#Click the mouse to set the color to track
s = 10

def setup():
    global video, trackColor
    size(320,240)
    video = Capture(this,320,240,30)
    video.start()


def draw():
    global video
    if (video.available()):
        video.read()
    
    for x in range(video.width /s ):
        for y in range(video.height /s ):
            loc = x * s + (y * s *(video.width))
            
            #what's the currentcolor
            currentColor = video.pixels[loc]
            #print loc, currentColor
            r1 = red(currentColor) + 59 
            g1 = green(currentColor)
            b1 = blue(currentColor)
            fill(r1,g1,b1)
            ellipse(x*s,y*s,s,s)
    
def mousePressed():
    global video
    pix = video.pixels[mouseX + mouseY*video.width]
    print red(pix),green(pix),blue(pix)