
from graph import brushColor, circle, penColor, penSize, moveTo, lineTo, rectangle, polygon, canvasSize, run
from math import sin, cos, pi, sqrt


def cloud(x, y, r):   # center of the upper left circle, rads
    brushColor('white')
    circle(x, y, r)
    circle(x + 1.5*r, y, r)
    circle(x - r, y + r, r)
    circle(x + 0.5*r, y + r, r)
    circle(x + 2*r, y + r, r)
    circle(x + 3*r, y, r)
    circle(x + 3.5*r, y + r, r)


def umbrella(x, y, h):   # where to put the leg, leg length
    penColor(170, 102, 0)
    penSize(h/20)
    moveTo(x, y)
    lineTo(x, y - h)
    penSize(0)
    brushColor(255, 88, 118)
    polygon([(x + h/40, y - h), (x - h/40, y - h), (x - h/2, y - 5/6*h), (x + h/2, y - 5/6*h)])
    penSize(3)
    penColor('brown')
    for i in range(3):   # lines on the umbrella
        moveTo(x - h/40, y - h)
        lineTo(x - h/2 + (i+1) * 0.15*h, y - 5/6*h)
    for i in range(3):
        moveTo(x + h/40, y - h)
        lineTo(x + h/2 - (i+1) * 0.15*h, y - 5/6*h)


def yacht(x, y, s):   # mast base coordinates, s  -  size (1>2>...)
    mast = 230/s   # mast high
    thi = 60/s   # yacht thickness
    bow = 100/s   # bow length
    col = 5/s   # mast column thickness
    # mast
    penSize(thi/5)
    penColor('black')
    moveTo(x, y)
    lineTo(x, y - mast)
    # sail
    penColor('white')
    brushColor(230, 230, 250)
    polygon([(x + col, y - mast), (x + col + bow, y - mast/2), (x + col + bow/4, y - mast/2)])
    polygon([(x + col, y), (x + col + bow, y - mast/2), (x + col + bow/4, y - mast/2)])
    # boat
    brushColor(170, 102, 0)
    penColor(170, 102, 0)
    rectangle(x - mast/2, y, x + mast/2, y + thi)
    polygon([(x + mast/2, y), (x + mast/2 + bow, y), (x + mast/2, y + thi)])
    for i in range(100):
        phi1 = i * pi / 200
        phi2 = (i+1) * pi / 200
        polygon([(x - mast/2 - thi*cos(phi1), y + thi*sin(phi1)), (x - mast/2 - thi*cos(phi2), y + thi*sin(phi2)),
                                                                  (x - mast/2, y)])
    # window
    penSize(0)
    brushColor('black')
    circle(x + mast/2 + bow/4, y + thi/3, thi/4)
    brushColor('white')
    circle(x + mast/2 + bow/4, y + thi/3, thi/6)


def sun(x, y, r, ray):  # center coordinates, rad, ray length + rad
    brushColor('yellow')
    penColor('yellow')
    penSize(0)
    v = 40   # number of rays
    for i in range(v):
        phi1 = 2 * i * pi / v
        phi2 = 2 * (i+1) * pi / v
        polygon([(x, y), (x + r*cos(phi1), y + r*sin(phi1)),
                         (x + ray*cos(phi1 + pi/v), y + ray*sin(phi1 + pi/v)), (x + r*cos(phi2), y + r*sin(phi2))])


def waves(y):   # y coordinate of bother between sea and sand
    penSize(0)
    r = 40
    n = 15
    for i in range(n):
        x = i * r * 2 * sqrt(3)
        brushColor(0, 0, 205)
        circle(x - r*sqrt(3)/2, y - r/2, r)
        brushColor(255, 229, 124)
        circle(x + r*sqrt(3)/2, y + r/2, r)


def view():
    # sky
    canvasSize(1000, 600)
    brushColor(135, 206, 250)
    rectangle(0, 0, 1000, 300)
    # sand
    brushColor(255, 229, 124)
    rectangle(0, 600, 1000, 500)
    # sea
    brushColor(0, 0, 205)  # море
    rectangle(0, 300, 1000, 500)

# lol
view()
waves(500)
sun(850, 100, 55, 80)
cloud(110, 65, 22)
cloud(470, 60, 42)
cloud(200, 160, 32)
umbrella(180, 570, 300)
umbrella(400, 550, 160)
yacht(750, 390, 1)
yacht(440, 325, 2)

run()
