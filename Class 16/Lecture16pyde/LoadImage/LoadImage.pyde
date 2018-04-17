#http://py.processing.org/tutorials/pixels/
def setup():
  global img
  size(320,240)
  # Make a new instance of a PImage by loading an image file
  # Declaring a variable of type PImage
  img = loadImage("lunar.jpg")

def draw():
  global img
  background(0);
  # Draw the image to the screen at coordinate (0,0)
  image(img,0,0)