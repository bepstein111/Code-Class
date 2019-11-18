add_library('opencv_processing')

img = None
opencv = None


def setup():
    global img,opencv
    img = loadImage("test.jpg")
    size(1020, 720)
    opencv = OpenCV(this, img)


def draw():
    global img,opencv
    opencv.loadImage(img)
    opencv.brightness(int(map(mouseX, 0, width, -255, 255)))
    image(opencv.getOutput(), 0, 0)
