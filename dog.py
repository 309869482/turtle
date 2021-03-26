import turtle as tt
from turtle import Screen

tt.bgpic()
# tt.bgpic("download.gif")
tt.title("Hello Cinnamoroll!")

tt.speed(10)
tt.penup()

#  head
tt.left(90)
tt.fd(200) 
tt.left(90)
tt.fd(200)
tt.pendown() 
tt.pensize(2)

tt.right(150)

tt.circle(-400, 60)

#  right ear
tt.left(45)
tt.circle(-160, 80)
tt.circle(80, 40)
tt.circle(-400, 20)
tt.circle(-80, 140)
tt.circle(-250, 30)
tt.circle(-700, 10)
tt.penup()

tt.home()

tt.left(90)
tt.fd(200) 
tt.left(90)
tt.fd(200)


#  left ear
tt.pendown()
tt.right(15)
tt.circle(160, 80)
tt.circle(-80, 40)
tt.circle(400, 20)
tt.circle(80, 140)
tt.circle(250, 30)
tt.circle(700, 10)

tt.penup()

#  right face
tt.home()
tt.left(90)
tt.fd(100)
tt.right(90)
tt.fd(250)
tt.pendown()
tt.right(60)
tt.circle(-150, 80)
tt.circle(-200, 30)
tt.circle(-680, 22)

tt.penup()

#  left face
tt.home()
tt.left(90)
tt.fd(100)
tt.left(90)
tt.fd(250)
tt.pendown()
tt.left(60)
tt.circle(150, 80)
tt.circle(200, 30)

tt.penup()

#  left eye
tt.home()
tt.left(90)
tt.fd(50)
tt.left(90)
tt.fd(150)
tt.pendown()
tt.fillcolor('#4169E1')
tt.begin_fill()
tt.right(15)
tt.circle(10, 70)
tt.circle(60, 40)
tt.circle(10, 140)
tt.circle(60, 40)
tt.circle(10, 70)
tt.end_fill()

tt.penup()

#  right eye
tt.home()
tt.left(90)
tt.fd(50)
tt.right(90)
tt.fd(150)
tt.pendown()
tt.fillcolor('#4169E1')
tt.begin_fill()
tt.left(15)
tt.circle(-10, 70)
tt.circle(-60, 40)
tt.circle(-10, 140)
tt.circle(-60, 40)
tt.circle(-10, 70)
tt.end_fill()

tt.penup()

#  left mouth
tt.home()
tt.right(90)
tt.fd(30)
tt.right(60)
tt.pendown()
tt.circle(-20, 60)
tt.circle(-10, 120)

tt.penup()

#  right mouth
tt.home()
tt.right(90)
tt.fd(30)
tt.left(60)
tt.pendown()
tt.circle(20, 60)
tt.circle(10, 120)

tt.penup()

#  left blush
tt.home()
tt.right(180)
tt.fd(150)
tt.left(90)
tt.fd(25)
tt.pendown()
tt.fillcolor('pink')
tt.begin_fill()
tt.circle(-15, 70)
tt.circle(-70, 40)
tt.circle(-15, 140)
tt.circle(-70, 40)
tt.circle(-15, 70)
tt.end_fill()

tt.penup()

#  right blush
tt.home()
tt.fd(150)
tt.right(90)
tt.fd(25)
tt.pendown()
tt.fillcolor('pink')
tt.begin_fill()
tt.circle(15, 70)
tt.circle(70, 40)
tt.circle(15, 140)
tt.circle(70, 40)
tt.circle(15, 70)
tt.end_fill()

tt.penup()

tt.home()
tt.fd(200)
tt.right(90)
tt.fd(200)
tt.write("Karen", True, align="center")



tt.exitonclick()