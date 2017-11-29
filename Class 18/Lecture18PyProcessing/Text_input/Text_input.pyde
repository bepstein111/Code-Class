settingsComplete = False
msg = ''
mymsg=''
def setup():
    size(400,300)

def draw():
    global settingsComplete,msg,mymsg
    if (settingsComplete==False):
        fill(255)
        rect(100,100,200,100)
        text("type your name", 120,120)
        fill(0)
        text(msg,122,120)
    elif settingsComplete:
        background(255)
        text('Hi '+mymsg, 132,130)
        
def keyPressed():
    global msg,mymsg,settingsComplete
    msg = msg + key
    print msg
    if key==ENTER:
        mymsg = msg
        settingsComplete = True