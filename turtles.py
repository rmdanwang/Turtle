
import turtle as t
wn = t.Screen()
wn.bgcolor("light green")
Alex = t.Turtle()
Alex.shape("turtle")
Alex.penup()
Alex.color("blue")
Alex.pensize(2)


for i in range(12):
    Alex.forward(100)
    Alex.stamp()
    Alex.backward(30)
    Alex.pendown()
    Alex.forward(10)
    Alex.penup()
    Alex.backward(80)
    Alex.right(30)

wn.exitonclick()
