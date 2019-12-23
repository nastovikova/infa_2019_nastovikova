import tkinter as tk
from random import randrange as rnd, choice

root = tk.Tk()
root.geometry('800x600')

i = 0
score = 0

label = tk.Label(root, bg='green', fg='yellow', width=50)
label.pack()

canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']


balls = []
rects = []


def rectangle():
    x1 = rnd(100, 200)
    y1 = rnd(100, 150)
    x2 = rnd(310, 400)
    y2 = rnd(300, 350)
    v_x = rnd(-10, 10)
    v_y = rnd(-10, 10)
    id_ = canv.create_rectangle(x1, y1, x2, y2, fill='pink',
                                activefill='yellow')
    rect = {'id': id_, 'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2,
            'v_x': v_x, 'v_y': v_y}
    rects.append(rect)
    root.after(5000, rectangle)


def move_rectangle():
    k = 0
    for b in rects:
        k = k + 0.1
        b['v_x'] += k
        b['v_y'] -= k
        if k % 1 == 0:
            b['v_y'] -= 5*k
        canv.coords(b['id'], b['v_x'] + b['x1'], b['v_y'] + b['y1'], b['v_x'] + b['y2'], b['v_y'] + b['y2'])
        b['y1'] += b['v_y']
        b['x1'] += b['v_x']
    root.after(40, move_rectangle)


def new_ball():
    global i
    i += 1
    x = rnd(100, 700)
    y = rnd(100, 500)
    v_x = rnd(-4, 4)
    v_y = rnd(-4, 4)
    r = rnd(30, 50)
    id_ = canv.create_oval(x - r, y - r, x + r, y + r, fill=choice(colors), width=0, activefill='red')
    ball = {'id': id_, 'x': x, 'y': y, 'r': r, 'v_x': v_x, 'v_y': v_y}
    balls.append(ball)
    root.after(2000 - i*1, new_ball)


def move_ball():
    k = 0
    for b in balls:
        k = k + 0.01
        if (b['x'] > 800 - b['r']) or (b['x'] < b['r']):
            b['v_x'] = -b['v_x']*1.106
        if (b['y'] > 600 - b['r']) or (b['y'] < b['r']):
            b['v_y'] = -b['v_y']*1.104
        b['v_x'] += k
        b['v_y'] -= k
        if k % 1 == 0:
            b['v_y'] -= 5*k
        canv.move(b['id'], b['v_x'], b['v_y'])
        b['y'] += b['v_y']
        b['x'] += b['v_x']
    root.after(10, move_ball)


def click(event):
    global score
    for k, b in enumerate(balls):
        if (event.x-b['x'])**2 + (event.y-b['y'])**2 <= b['r']**2:
            canv.delete(b['id'])
            del balls[k]
            score += 1
            label['text'] = 'Score:' + str(score)
    for k, b in enumerate(rects):
        if event.x >= min(b['x1'], b['x2']) and event.x <= max(b['x1'], b['x2']) and event.y >= min(b['y1'], b['y2']) and event.y <= max(b['y1'], b['y2']):
            canv.delete(b['id'])
            del rects[k]
            score += 5
            label['text'] = 'Score:' + str(score)


new_ball()
rectangle()
move_rectangle()
move_ball()
canv.bind('<Button-1>', click)
tk.mainloop()
