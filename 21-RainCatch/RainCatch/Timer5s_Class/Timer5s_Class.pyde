from Timer import Timer

timer = None

def setup():
    global timer
    size(200,200)
    background(0)
    timer = Timer(5000)
    timer.start()

def draw():
    global timer
    if (timer.isFinished()):
        background(random(255))
        timer.start()
    