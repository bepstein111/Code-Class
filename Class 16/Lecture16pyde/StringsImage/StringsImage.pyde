#http://py.processing.org/tutorials/pixels/
def setup():
  frameRate(20)
  global img
  global lines
  global index
  size(320,240)
  #load lines and image
  lines = loadStrings("lovesong.txt")
  img = loadImage("lunar.jpg")
  index = 0

def draw():
  global img
  global lines
  global index
  background(0)
  
  # Draw the image to the screen at coordinate (0,0)
  image(img,0,0)
  if (frameCount % 40 ==0):
      index = (index +1) % len(lines)
  text(lines[index],20,20,300,50)
  