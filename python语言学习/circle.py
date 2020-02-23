import turtle
turtle.setup(600,400,220,220)

turtle.penup()
turtle.left(150)
turtle.fd(300)
turtle.pendown()
turtle.right(150)

for i in range(1,5):
    turtle.pencolor("blue")
    turtle.pensize(5)
    turtle.circle(-100,90)

    turtle.pencolor("yellow")
    turtle.pensize(5)
    turtle.fd(150)

    turtle.fd(-150)
    turtle.pencolor("red")
    turtle.pensize(5)


    turtle.right(180)
    
    turtle.circle(-100,90)

turtle.circle(-100,90)
turtle.circle(-100,90)
turtle.pencolor("purple")
turtle.fd(800)
turtle.circle(-100,90)
turtle.circle(-100,90)


