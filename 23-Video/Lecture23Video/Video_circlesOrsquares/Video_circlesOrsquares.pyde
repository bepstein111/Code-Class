add_library('video')

s = 10
h = False
saveimage = False
message= """Click mouse for color of a pixel.\n
     Press: 4(decrease),5(increase),c(circles),s(squares)"""
def setup():
    global video, trackColor, mode,s
    size(320,240)
    video = Capture(this,320,240,30)
    video.start()
    noStroke()
    rectMode(CENTER)
    ellipseMode(CENTER)
    mode = 's'
    s = 20
    h = False
    saveimage = False
    

def draw():
    global video,mode,s,h, message,saveimage
    if (video.available()):
        video.read()
    if s<1:
        s = 5
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
            if mode == 'c':
                ellipse( x*s + s/2, y*s +s/2,s,s)
            else:
                rect(x*s + s/2, y*s +s/2 ,s,s)
            if h:
                text(message, 10, height-20, width,20)
    if saveimage:
        stroke(0,255,0)
        saveFrame("img##.png")
        line(0,height-1,width,height-1)
    else:
        stroke(255,0,0)
    noStroke()
        
                
def mousePressed():
    #print status
    global video, s, h, mode, saveimage
    pix = video.pixels[mouseX + mouseY*video.width]
    print "color: ",red(pix),green(pix),blue(pix),"mode: ", \
    mode, "size: ", s,"saving: ", saveimage
    saveimage = not saveimage
#change modes
def keyPressed():
    global mode,s,h
    if key=='s':
        mode = "s"
    if key=='c':
        mode = 'c'
    if key=='5':
        s = s+5
    if key=='4':
        s = s-5
    if key=='h':
        h = not h
