add_library('video')

def setup():
    global video
    size(320,240)
    video = Capture(this,320,240,15)
    video.start()
    background(0)

def draw():
    global video
    if (video.available()):
        video.read()
    set(0,0, video)
    