import turtle

canvas = turtle.Screen()

v_pen =turtle.Turtle()
v_pen.pensize(5)
v_pen.pencolor("red")
for i in range(6):
    v_pen.forward(100)
    v_pen.right(60)  # Pentagon 360/5 = 72
                     # hexagon 360/6 = 60


v_pen.hideturtle()
canvas.exitonclick()