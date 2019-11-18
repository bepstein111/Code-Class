# Learning Processing
# Daniel Shiffman 
# http:#www.learningprocessing.com
# translated to Python by anjchang
# Example 16-1: Display video

# Step 1. Import the video library
add_library('video')

# Step 2. Declare a Capture object
video = None

def setup():
  global video  #make video available
  size(320, 240)       #set up display size
  println(Capture.list()) #print all system camera options
  # Step 3. Initialize Capture object via Constructor
  # Use the default camera at 320x240 resolution
  video = Capture(this, 320, 240)
  video.start()

# An event for when a new frame is available
def captureEvent( video):
  # Step 4. Read the image from the camera.
  video.read()

def draw():
  global video #look elsewhere for video
  # Step 5. Display the video image.
  image(video, 0, 0)