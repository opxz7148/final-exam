import turtle
import random

# specify a reduction ratio to draw a smaller polygon inside the one above

reduction_ratio = 0.618

class Canva:

    def __init__(self):
        self.choice = int(input("Which art do you want to generate? Enter a number between 1 to 8, inclusive: "))


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

    def reduction(self):



def draw_polygon(num_sides, size, orientation, location, color, border_size):
    turtle.penup()
    turtle.goto(location[0], location[1])
    turtle.setheading(orientation)
    turtle.color(color)
    turtle.pensize(border_size)
    turtle.pendown()
    for _ in range(num_sides):
        turtle.forward(size)
        turtle.left(360/num_sides)
    turtle.penup()

def get_new_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#
turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)

# draw a polygon at a random location, orientation, color, and border line thickness
num_sides = random.randint(3, 5) # triangle, square, or pentagon
size = random.randint(50, 150)
orientation = random.randint(0, 90)
location = [random.randint(-300, 300), random.randint(-200, 200)]
color = get_new_color()
border_size = random.randint(1, 10)
draw_polygon(num_sides, size, orientation, location, color, border_size)



# reposition the turtle and get a new location
turtle.penup()
turtle.forward(size*(1-reduction_ratio)/2)
turtle.left(90)
turtle.forward(size*(1-reduction_ratio)/2)
turtle.right(90)
location[0] = turtle.pos()[0]
location[1] = turtle.pos()[1]

# adjust the size according to the reduction ratio
size *= reduction_ratio

# draw the second polygon embedded inside the original
draw_polygon(num_sides, size, orientation, location, color, border_size)

# hold the window; close it by clicking the window close 'x' mark


poly1 = Polygon(4,100, 60, [122, -150], get_new_color(), 3)
poly1.draw()

turtle.done()