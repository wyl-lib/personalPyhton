#heart painting

from turtle import *
setup(1040,420,200,200)
pensize(16)
pencolor("red")

fd(100)
fd(-50)
right(90)
fd(200)
right(90)
fd(50)
fd(-100)

penup()
fd(-100)
left(90)
fd(-100)
right(45)
fd(-100)
pendown()


left(135)
fd(100)
fd(-100)
right(90)
fd(100)
fd(-100)
left(45)
fd(-180)

#penup()
#fd(300)
#left(90)
#fd(-20)
#pendown()

penup()
fd(-100)
seth(-105)
fd(100)
right(135)
pendown()
color('yellow','red')
begin_fill()
circle(-240,15)
circle(-20,160)
seth(45)
circle(-20,160)
circle(-280,15)
end_fill()
done()
