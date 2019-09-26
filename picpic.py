from graph import *
from math import *

canvasSize(1000,600)
brushColor(0, 191, 255)
penSize(0)
rectangle(0, 0, 1000, 300)
brushColor(255, 229, 124)
rectangle(0, 600, 1000, 500)
brushColor(0, 0, 205)
rectangle(0, 300, 1000, 500)
brushColor('yellow')
circle(860, 75, 60)

def cloud(x, y, r): # центр левого верхнего круга, радиусы
    brushColor('white')
    circle(x, y, r)
    circle(x+1.5*r, y, r)
    circle(x-r, y+r, r)
    circle(x+0.5*r, y+r, r)
    circle(x+2*r, y+r, r)
    circle(x+3*r, y, r)
    circle(x+3.5*r, y+r, r)

cloud(250, 150, 30) 

def umbrella(x, y, h): # куда воткнули ножку, длина ножки
    penColor(170, 102, 0)
    penSize(h/20)
    moveTo(x,y)
    lineTo(x,y-h)
    penSize(0)
    brushColor(255, 88, 118)
    polygon([(x+h/40,y-h), (x-h/40,y-h), (x-h/2,y-5/6*h), (x+h/2,y-5/6*h)])
    penSize(3)
    penColor('brown')
    for i in range(3):
        moveTo(x-h/40,y-h)
        lineTo(x-h/2+(i+1)*0.15*h, y-5/6*h)
    for i in range(3):
        moveTo(x+h/40,y-h)
        lineTo(x+h/2-(i+1)*0.15*h, y-5/6*h)

umbrella(180, 570, 300) 

def yacht(x, y, s): # x,y основание мачты, s - размер (1>2>...)
    a = 230/s # высота мачты
    b = 60/s # толщина яхты
    c = 100/s # длина носа
    d = 5/s # толщина мачты
    penSize(b/5)
    penColor('black')
    moveTo(x, y)
    lineTo(x, y-a)
    penSize(b/15)
    penColor('white')
    brushColor(230, 230, 250)
    polygon([(x+d,y-a), (x+d+c,y-a/2), (x+d+c/4,y-a/2)])
    polygon([(x+d,y), (x+d+c,y-a/2), (x+d++c/4,y-a/2)])
    brushColor(170, 102, 0)
    penColor(170, 102, 0)
    rectangle(x-a/2, y, x+a/2, y+b)
    polygon([(x+a/2,y), (x+a/2+c,y), (x+a/2,y+b)])
    
    for i in range(100): # сегмент 
        phi1 = i*pi/200
        phi2 = (i+1)*pi/200
        polygon([(x-a/2 - b*cos(phi1), y + b*sin(phi1)), (x-a/2 - b*cos(phi2), y + b*sin(phi2)), (x-a/2, y)])

    penSize(0)
    brushColor('black')
    circle(x+a/2+c/4, y+b/3, b/4)
    brushColor('white')
    circle(x+a/2+c/4, y+b/3, b/6)
    

yacht(600, 390, 1)

run()
