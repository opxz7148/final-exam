import turtle
import random

# specify a reduction ratio to draw a smaller polygon inside the one above

reduction_ratio = 0.618

class Canva:

    def __init__(self):

        self.level = 1
        self.rand1 = 0
        self.rand2 = 0
        self.choice = int(input("Which art do you want to generate? Enter a number between 1 to 8, inclusive: "))
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)
        self.setting_art()

    def setting_art(self):

        if self.choice == 1:
            self.rand1, self.rand2 = 3, 3

        elif self.choice == 2:
            self.rand1, self.rand2 = 4, 4

        elif self.choice == 3:
            self.rand1, self.rand2 = 5, 5

        elif self.choice == 4:
            self.rand1, self.rand2 = 3, 5

        elif self.choice == 5:
            self.rand1, self.rand2 = 3, 3
            self.level = 3

        elif self.choice == 6:
            self.rand1, self.rand2 = 4, 4
            self.level = 3

        elif self.choice == 7:
            self.rand1, self.rand2 = 5, 5
            self.level = 3

        elif self.choice == 8:
            self.rand1, self.rand2 = 3, 5
            self.level = 3

    def make_art(self):
        for _ in range(random.randint(20, 40)):
            poly = Polygon(
                num_sides=random.randint(self.rand1, self.rand2),
                size=random.randint(50, 150),
                orientation=random.randint(0, 90),
                location=[random.randint(-300, 300), random.randint(-200, 200)],
                color=self.get_new_color(),
                border_size=random.randint(1, 10),
                level=self.level
            )
            poly.draw()

    def get_new_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))



class Polygon:

    def __init__(self, num_sides, size, orientation, location, color, border_size, level=1):
        self.num_sides = num_sides
        self.size = size
        self.orien = orientation
        self.location = location
        self.color = color
        self.border_size = border_size
        self.level = level

    def draw(self):

        for _ in range(self.level):

            turtle.penup()
            turtle.goto(self.location[0], self.location[1])
            turtle.setheading(self.orien)
            turtle.color(self.color)
            turtle.pensize(self.border_size)
            turtle.pendown()

            for _ in range(self.num_sides):
                turtle.forward(self.size)
                turtle.left(360 / self.num_sides)
            turtle.penup()

            self.reduction()

    def reduction(self):

        turtle.penup()
        turtle.forward(self.size * (1 - reduction_ratio) / 2)
        turtle.left(90)
        turtle.forward(self.size * (1 - reduction_ratio) / 2)
        turtle.right(90)
        self.location[0] = turtle.pos()[0]
        self.location[1] = turtle.pos()[1]

        self.size *= reduction_ratio


canva1 = Canva()
canva1.make_art()

turtle.done()