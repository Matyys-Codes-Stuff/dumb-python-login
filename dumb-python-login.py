from turtle import *
from random import *
import random
import time
import pygame
import sys

print(" ")
print("Run in Thonny!")
print(" ")
time.sleep(5)

qwe = "A"
rty = "1"
asd = "d"
uio = "2"
fgh = "3"
jkl = "m"
zxc = "4"
vbn = "i"
bnm = "5"
ewq = "n"

def hp():
    if what == "help":
        print(" ")
        print("    Yingyang")
        print("    Linden Mayer")
        print("    Planet and Moon")
        print("    Tetris")
        print(" ")
        print("Run this script again!")
        time.sleep(10)

print("Log in: Admin    Log in: Testing")
print("Password: 12345  Password: -")
print(" ")
nm = input("Log in as: ")
if nm == "Testing":
    import turtle
    text = textinput("Select test", " ")
    
    if text == "Test1":
        import turtle
        turtle.title("Square")
        forward(300)
        left(90)
        forward(300)
        left(90)
        forward(300)
        left(90)
        forward(300)
        left(90)
        forward(150)
        left(90)
        
        turtle.done()
        bye()
                
    if text == "Test2":
        import turtle
        turtle.title("Star")
        def draw_star(size):
            for _ in range(5):
                turtle.forward(size)
                turtle.right(144)  # Otočení o 144 stupňů

        # Nastavení turtle
        turtle.speed(3)  # Nastavení rychlosti kreslení
        turtle.color("blue")  # Nastavení barvy

        # Kreslení hvězdy
        for i in range(6):
            draw_star(100)  # Velikost hvězdy
            turtle.right(72)  # Otočení hvězdy pro vytvoření složitějšího tvaru

        turtle.done()
          
    bye()

else:
    if nm == qwe+asd+jkl+vbn+ewq:
        psw = input("Password: ")
        
    if psw == rty+uio+fgh+zxc+bnm:
        print(" ")
        print("Type help if needed!")
        print(" ")
        what = input("What do you want: ")
        if what == "help":
            hp()
        
        if what == "Yingyang":

            def yin(radius, color1, color2):
                width(3)
                color("black", color1)
                begin_fill()
                circle(radius/2., 180)
                circle(radius, 180)
                left(180)
                circle(-radius/2., 180)
                end_fill()
                left(90)
                up()
                forward(radius*0.35)
                right(90)
                down()
                color(color1, color2)
                begin_fill()
                circle(radius*0.15)
                end_fill()
                left(90)
                up()
                backward(radius*0.35)
                down()
                left(90)

            def main():
                reset()
                yin(200, "black", "white")
                yin(200, "white", "black")
                ht()
                return "Done!"

            if __name__ == '__main__':
                main()
                print(" ")
                print("Done :)")
                time.sleep(5)
                screen.mainloop()
                
        if what == "Linden Mayer":
            
            def replace( seq, replacementRules, n ):
                for i in range(n):
                    newseq = ""
                    for element in seq:
                        newseq = newseq + replacementRules.get(element,element)
                    seq = newseq
                return seq

            def draw( commands, rules ):
                for b in commands:
                    try:
                        rules[b]()
                    except TypeError:
                        try:
                            draw(rules[b], rules)
                        except:
                            pass


            def main():
                ################################
                # Example 1: Snake kolam
                ################################


                def r():
                    right(45)

                def l():
                    left(45)

                def f():
                    forward(7.5)

                snake_rules = {"-":r, "+":l, "f":f, "b":"f+f+f--f--f+f+f"}
                snake_replacementRules = {"b": "b+f+b--f--b+f+b"}
                snake_start = "b--f--b--f"

                drawing = replace(snake_start, snake_replacementRules, 3)

                reset()
                speed(3)
                tracer(1,0)
                ht()
                up()
                backward(195)
                down()
                draw(drawing, snake_rules)

                from time import sleep
                sleep(3)

                ################################
                # Example 2: Anklets of Krishna
                ################################

                def A():
                    color("red")
                    circle(10,90)

                def B():
                    from math import sqrt
                    color("black")
                    l = 5/sqrt(2)
                    forward(l)
                    circle(l, 270)
                    forward(l)

                def F():
                    color("green")
                    forward(10)

                krishna_rules = {"a":A, "b":B, "f":F}
                krishna_replacementRules = {"a" : "afbfa", "b" : "afbfbfbfa" }
                krishna_start = "fbfbfbfb"

                reset()
                speed(0)
                tracer(3,0)
                ht()
                left(45)
                drawing = replace(krishna_start, krishna_replacementRules, 3)
                draw(drawing, krishna_rules)
                tracer(1)
                print(" ")
                return "Done :)"

            if __name__=='__main__':
                msg = main()
                print(msg)
                time.sleep(5)
                screen.mainloop()
        
        if what == "Planet and Moon":
            from turtle import Shape, Turtle, mainloop, Vec2D as Vec

            G = 8

            class GravSys(object):
                def __init__(self):
                    self.planets = []
                    self.t = 0
                    self.dt = 0.01
                def init(self):
                    for p in self.planets:
                        p.init()
                def start(self):
                    for i in range(1500):
                        self.t += self.dt
                        for p in self.planets:
                            p.step()

            class Star(Turtle):
                def __init__(self, m, x, v, gravSys, shape):
                    Turtle.__init__(self, shape=shape)
                    self.penup()
                    self.m = m
                    self.setpos(x)
                    self.v = v
                    gravSys.planets.append(self)
                    self.gravSys = gravSys
                    self.resizemode("user")
                    self.pendown()
                def init(self):
                    dt = self.gravSys.dt
                    self.a = self.acc()
                    self.v = self.v + 0.5*dt*self.a
                def acc(self):
                    a = Vec(0,0)
                    for planet in self.gravSys.planets:
                        if planet != self:
                            v = planet.pos()-self.pos()
                            a += (G*planet.m/abs(v)**3)*v
                    return a
                def step(self):
                    dt = self.gravSys.dt
                    self.setpos(self.pos() + dt*self.v)
                    if self.gravSys.planets.index(self) != 0:
                        self.setheading(self.towards(self.gravSys.planets[0]))
                    self.a = self.acc()
                    self.v = self.v + dt*self.a

            ## create compound yellow/blue turtleshape for planets

            def main():
                s = Turtle()
                s.reset()
                s.getscreen().tracer(0,0)
                s.ht()
                s.pu()
                s.fd(6)
                s.lt(90)
                s.begin_poly()
                s.circle(6, 180)
                s.end_poly()
                m1 = s.get_poly()
                s.begin_poly()
                s.circle(6,180)
                s.end_poly()
                m2 = s.get_poly()

                planetshape = Shape("compound")
                planetshape.addcomponent(m1,"orange")
                planetshape.addcomponent(m2,"blue")
                s.getscreen().register_shape("planet", planetshape)
                s.getscreen().tracer(1,0)

                ## setup gravitational system
                gs = GravSys()
                sun = Star(1000000, Vec(0,0), Vec(0,-2.5), gs, "circle")
                sun.color("yellow")
                sun.shapesize(1.8)
                sun.pu()
                earth = Star(12500, Vec(210,0), Vec(0,195), gs, "planet")
                earth.pencolor("green")
                earth.shapesize(0.8)
                moon = Star(1, Vec(220,0), Vec(0,295), gs, "planet")
                moon.pencolor("gray")
                moon.shapesize(0.5)
                gs.init()
                gs.start()
                return "Done!"

            if __name__ == '__main__':
                main()
                print(" ")
                print("Done :)")
                time.sleep(5)
                screen.mainloop()
                
        if what == "Tetris":
            print(" ")

            colors = [
                (0, 0, 0),
                (120, 37, 179),
                (100, 179, 179),
                (80, 34, 22),
                (80, 134, 22),
                (180, 34, 22),
                (180, 34, 122),
            ]


            class Figure:
                x = 0
                y = 0

                figures = [
                    [[1, 5, 9, 13], [4, 5, 6, 7]],
                    [[4, 5, 9, 10], [2, 6, 5, 9]],
                    [[6, 7, 9, 10], [1, 5, 6, 10]],
                    [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
                    [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
                    [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
                    [[1, 2, 5, 6]],
                ]

                def __init__(self, x, y):
                    self.x = x
                    self.y = y
                    self.type = random.randint(0, len(self.figures) - 1)
                    self.color = random.randint(1, len(colors) - 1)
                    self.rotation = 0

                def image(self):
                    return self.figures[self.type][self.rotation]

                def rotate(self):
                    self.rotation = (self.rotation - 1) % len(self.figures[self.type])


            class Tetris:
                def __init__(self, height, width):
                    self.level = 2
                    self.score = 0
                    self.state = "start"
                    self.field = []
                    self.height = 0
                    self.width = 0
                    self.x = 100
                    self.y = 60
                    self.zoom = 20
                    self.figure = None
                
                    self.height = height
                    self.width = width
                    self.field = []
                    self.score = 0
                    self.state = "start"
                    for i in range(height):
                        new_line = []
                        for j in range(width):
                            new_line.append(0)
                        self.field.append(new_line)

                def new_figure(self):
                    self.figure = Figure(3, 0)

                def intersects(self):
                    intersection = False
                    for i in range(4):
                        for j in range(4):
                            if i * 4 + j in self.figure.image():
                                if i + self.figure.y > self.height - 1 or \
                                        j + self.figure.x > self.width - 1 or \
                                        j + self.figure.x < 0 or \
                                        self.field[i + self.figure.y][j + self.figure.x] > 0:
                                    intersection = True
                    return intersection

                def break_lines(self):
                    lines = 0
                    for i in range(1, self.height):
                        zeros = 0
                        for j in range(self.width):
                            if self.field[i][j] == 0:
                                zeros += 1
                        if zeros == 0:
                            lines += 1
                            for i1 in range(i, 1, -1):
                                for j in range(self.width):
                                    self.field[i1][j] = self.field[i1 - 1][j]
                    self.score += lines ** 2

                def go_space(self):
                    while not self.intersects():
                        self.figure.y += 1
                    self.figure.y -= 1
                    self.freeze()

                def go_down(self):
                    self.figure.y += 1
                    if self.intersects():
                        self.figure.y -= 1
                        self.freeze()

                def freeze(self):
                    if event.key != pygame.K_SPACE:
                        time.sleep(0.8)
                    for i in range(4):
                        for j in range(4):
                            if i * 4 + j in self.figure.image():
                                self.field[i + self.figure.y][j + self.figure.x] = self.figure.color
                    self.break_lines()
                    self.new_figure()
                    if self.intersects():
                        self.state = "gameover"

                def go_side(self, dx):
                    old_x = self.figure.x
                    self.figure.x += dx
                    if self.intersects():
                        self.figure.x = old_x

                def rotate(self):
                    old_rotation = self.figure.rotation
                    self.figure.rotate()
                    if self.intersects():
                        self.figure.rotation = old_rotation


            # Initialize the game engine
            pygame.init()

            # Define some colors
            BLACK = (0, 0, 0)
            WHITE = (255, 255, 255)
            GRAY = (128, 128, 128)

            size = (400, 500)
            screen = pygame.display.set_mode(size)

            pygame.display.set_caption("Tetris")

            # Loop until the user clicks the close button.
            done = False
            clock = pygame.time.Clock()
            fps = 25
            game = Tetris(20, 10)
            counter = 0

            pressing_down = False

            while not done:
                if game.figure is None:
                    game.new_figure()
                counter += 1
                if counter > 100000:
                    counter = 0

                if counter % (fps // game.level // 2) == 0 or pressing_down:
                    if game.state == "start":
                        game.go_down()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            game.rotate()
                            pressing_down = False
                        if event.key == pygame.K_DOWN:
                            pressing_down = True
                        if event.key == pygame.K_LEFT:
                            game.go_side(-1)
                            pressing_down = False
                        if event.key == pygame.K_RIGHT:
                            game.go_side(1)
                            pressing_down = False
                        if event.key == pygame.K_SPACE:
                            game.go_space()
                            pressing_down = False
                        if event.key == pygame.K_ESCAPE:
                            game.__init__(20, 10)

                if event.type == pygame.KEYUP:
                        if event.key == pygame.K_DOWN:
                            pressing_down = False

                screen.fill(BLACK)

                for i in range(game.height):
                    for j in range(game.width):
                        pygame.draw.rect(screen, GRAY, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
                        if game.field[i][j] > 0:
                            pygame.draw.rect(screen, colors[game.field[i][j]],
                                             [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

                if game.figure is not None:
                    for i in range(4):
                        for j in range(4):
                            p = i * 4 + j
                            if p in game.figure.image():
                                pygame.draw.rect(screen, colors[game.figure.color],
                                                 [game.x + game.zoom * (j + game.figure.x) + 1,
                                                  game.y + game.zoom * (i + game.figure.y) + 1,
                                                  game.zoom - 2, game.zoom - 2])

                font = pygame.font.SysFont('Calibri', 25, True, False)
                font1 = pygame.font.SysFont('Calibri', 65, True, False)
                text = font.render("Score: " + str(game.score), True, WHITE)
                text_game_over = font1.render("Game Over", True, (255, 125, 0))
                text_game_over1 = font1.render("Press ESC", True, (255, 215, 0))

                screen.blit(text, [0, 0])
                if game.state == "gameover":
                    screen.blit(text_game_over, [20, 200])
                    screen.blit(text_game_over1, [25, 265])

                pygame.display.flip()
                clock.tick(fps)

            pygame.quit()



