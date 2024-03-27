import turtle


class turtleFunctions():
    def draw_sun(self):
        sun = turtle.Turtle()

        sun.speed(20)

        for i in range(36):
            sun.forward(100)
            sun.right(170)

        sun.hideturtle()
        turtle.done()

    def draw_star(self):
        star = turtle.Turtle()

        star.speed(5)

        for i in range(5):
            star.forward(100)
            star.right(144)

        star.hideturtle()
        turtle.done()
