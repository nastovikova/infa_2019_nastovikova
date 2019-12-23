from random import randrange as rnd, choice
import tkinter as tk
import math
import time

# print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)
g = 3


class ball():

    global t2, t1

    def __init__(self, x=40, y=450):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 180

    def set_coords(self):
        canv.coords(self.id,
                    self.x - self.r,
                    self.y - self.r,
                    self.x + self.r,
                    self.y + self.r)

    def move(self):
        """Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME
        if self.x + self.vx >= 780 or self.x + self.vx <= 15:
            self.vx = -self.vx*0.85
        if self.y - self.vy >= 580 or self.y - self.vy <= 15:
            self.vy = -self.vy*0.85
        else:
            self.vy = self.vy-g
        """"if abs(self.vy) <= 1:
            self.vy = 0
            self.live = 0"""
        self.x += self.vx
        self.y -= self.vy
        self.set_coords()
        self.live -= 1

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME
        if (self.x - obj.x) ** 2 + (self.y-obj.y)**2 <= (self.r + obj.r) ** 2:
            return True
        else:
            return False


class gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20, 450, 50, 420, width=7)
        # FIXME: don't know how to set it...
        self.y = 450
        self.x = 20

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball(self.x, self.y)
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y-self.y) / (event.x-20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, self.y,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    self.y + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, self.y,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    self.y + max(self.f2_power, 20) * math.sin(self.an))

    def move_up(self, event):
        if self.y > 150:
            self.y -= 1
            canv.coords(self.id, 20, self.y,
                        20 + max(self.f2_power, 20) * math.cos(self.an),
                        self.y + max(self.f2_power, 20) * math.sin(self.an))

    def move_down(self, event):
        if self.y < 500:
            self.y += 1
            canv.coords(self.id, 20, self.y,
                        20 + max(self.f2_power, 20) * math.cos(self.an),
                        self.y + max(self.f2_power, 20) * math.sin(self.an))


class target():
    def __init__(self):
        self.points = 0
        self.live = 1
        # FIXME:don't work!!! How to call this functions when object is created?
        self.id = canv.create_oval(0, 0, 0, 0)
        self.id_points = canv.create_text(30, 30, text=self.points, font='28')
        self.new_target()
        self.dx = rnd(-3, 3)
        self.dy = rnd(-3, 3)

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        color = self.color = 'red'
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        canv.itemconfig(self.id_points, text=self.points)

    def mv(self, inst):
        if self.x + self.dx >= 780 or self.x + self.dx <= 15:
            self.dx = -self.dx
        if self.y + self.dy >= 580 or self.y+self.dy <= 15:
            self.dy = -self.dy
        self.x = self.x+self.dx
        self.y = self.y+self.dy
        canv.delete(self, self.id)
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color)
        for i in inst:
            if i != self:
                if (self.x-i.x)**2 + (self.y-i.y)**2 <= (self.r+i.r)**2:
                    self.dx = -self.dx
                    self.dy = -self.dy
                    i.dx = -i.dx
                    i.dy = -i.dy


t1 = target()
t2 = target()
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
bullet = 0
balls = []


def new_game(event=''):
    global gun, t1, t2, screen1, balls, bullet
    canv.itemconfig(screen1, text='')
    t1.new_target()
    t2.new_target()

    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)
    root.bind('<Up>', g1.move_up)
    root.bind('<Down>', g1.move_down)
    t1.live = 1
    t2.live = 1
    while (t1.live > 0 and t2.live > 0) or balls:
        t2.mv([t1, t2])
        t1.mv([t1, t2])
        for i, b in enumerate(balls):
            b.move()
            if b.live <= 0:
                canv.delete(b.id)
            if (b.hittest(t1) or b.hittest(t2)) and t1.live > 0 and t2.live > 0:
                t1.live = 0
                t2.live = 0
                t1.hit()
                t2.hit()
                canv.bind('<Button-1>', "")
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text='Вы уничтожили цели за ' + str(bullet) + ' выстрелов')
                for bb in balls:
                    canv.delete(bb.id)
                balls = []
        canv.update()
        time.sleep(0.03)
        g1.power_up()
    canv.itemconfig(screen1, text='')
    canv.delete(gun)
    time.sleep(0.3)
    root.after(750, new_game)


new_game()

root.mainloop()
