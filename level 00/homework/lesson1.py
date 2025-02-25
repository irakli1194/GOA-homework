from turtle import * 

# we want to pain a house

shape("turtle")
speed(40)
width(7)
color ("purple")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

begin_fill()
forward(70)
color("green")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()

color("blue")


begin_fill()

right(150)
forward(200)
left(120)
forward(200)


end_fill()


color("brown")

begin_fill()
left(30)
forward(60)
left(90)
forward(40)
right(90)
forward(60)
right(90)
forward(40)

end_fill()

penup()
goto(200,200)
pendown()

color("brown")

begin_fill()

left(90)
forward(60)
right(90)
forward(40)
left(90)
forward(60)
left(90)
forward(40)

end_fill()





# step one draw a squre







exitonclick()