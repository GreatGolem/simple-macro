from PIL import Image,ImageGrab

#screenshot = ImageGrab.grab()
#screenshot.save("test.png","PNG")
#rgb = screenshot.getpixel((100,100))
#print rgb #(33,37,43)
#print rgb[1]

def pixel_color(x,y):
    return ImageGrab.grab().getpixel((x,y))

#print pixel_color(100,100)
