from Tkinter import *
import win32api
import capture_scr as scr

def get_mouse_position():

    root = Tk()

    def key(event):
        global mousex,mousey,mouseColor
        mousex,mousey = win32api.GetCursorPos()
        mouseColor = scr.pixel_color(mousex,mousey)
        print "mouse position", mousex, mousey
        print "mouse pixel color", mouseColor
        root.destroy()

#    def callback(event):
#        print "clicked at", event.x, event.y

    frame = Frame(root, width=100, height=50)
    frame.bind("<space>", key)
    frame.pack()
    frame.focus_force()

    root.mainloop()

#    print mousex,mousey
    return [mousex,mousey,[mouseColor[0],mouseColor[1],mouseColor[2]]]

#get_mouse_position()
