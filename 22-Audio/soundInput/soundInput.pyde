add_library('sound')
mic = None
amp = None
def setup():
    global mic, amp
    size(440,440)
    background(0)
    #Create an audio input and start it
    mic = AudioIn(this,0)
    mic.start()
    #Create a new amplitude analyzer and patch into input
    amp = Amplitude(this)
    amp.input(mic)
    
def draw():
    #draw a background that fades to black
    noStroke()
    fill(26, 76, 102, 10)
    rect(0,0, width, height)
    # Analyze() returns values between 0 and 1
    #so map() is used to convert values to larger numbers
    diameter = map(amp.analyze(),0,1, 10, width)
    # Draw circle based on the voume
    fill(255)
    ellipse(width/2, height/2, diameter, diameter)
    