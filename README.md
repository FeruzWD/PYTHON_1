import random
import math
from tkinter import Tk, Canvas, PhotoImage, mainloop

width = 1000
height = 600
window = Tk()
canvas = Canvas(window, width=width, height=height, bg="lightgray")
canvas.pack()
img = PhotoImage(width=width, height=height)
canvas.create_image((width//2, height//2), image=img, state="normal")
y = int (height/2)
for x in range (width):
    img.put ("#ffffff", (x, y))
x = int (width/2)
for y in range (height):
    img.put ("#ffffff", (x, y))
def center_and_invert_y(y, height):
    return int(height/2 - y)
def center_and_invert_x(x, width):
    return int(width/2 - x)
def ROUND(a):
    return int(a + 0.5)
#def signum (a):
#    return (1 if a > 0 else -1 if dx < 0 else 0)

def drawBrezenx(x1,y1,x2,y2):
     dx = x2 - x1
     dy = y2 - y1

     signx = 1 if dx > 0 else -1 if dx < 0 else 0
     signy = 1 if dy > 0 else -1 if dy < 0 else 0

     if dx < 0: dx = -dx
     if dy < 0: dy = -dy

     if dx > dy:
             pdx = signx
             pdy = dx - dx
             es, el = dy, dx
     else:
             pdx, pdy = 0, signy
             es, el = dx, dy
     x, y = x1, y1
     
     error, t = el / 2, 0
     xx = int (width/2) + x
     yy = int (height/2) + y

     img.put("#000000", (ROUND(x), ROUND(y)))

     while t < el:
             error -= es
             if error < 0:
                 error += el
                 x += signx
                 y += signy
             else:
                 x += pdx
                 y += pdy
             t += 1
             xx = int (width/2) + x
             yy = int (height/2) + y
             img.put("#000000", (ROUND(xx), ROUND(yy)))

drawBrezenx(0,0,300,-100)    ?
drawBrezenx(0,0,300,-100)    ?
drawBrezenx(0,0,300,-100)    ?
drawBrezenx(0,0,300,-100)    ?
