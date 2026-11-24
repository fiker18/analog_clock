#from turtle import *
import turtle
from datetime import datetime


minutes = 60
screen = turtle.Screen()

# Writing the tile of the project

title = turtle.Turtle()
title.teleport(-150, 350)
title.write("Analog Clock", font=("Helvetica", 48, "bold"))
title.forward(300)

title.hideturtle()

# creating a turtle to draw the clock 

arrow = turtle.Turtle()

arrow.teleport(0, 250)
home = arrow.pos() 

arrow.color("black", "blue")
arrow.begin_fill()

arrow.circle(-250)
arrow.end_fill()



#setup using a loop that draws the lines with diffrent tickness every 6 degrees and names some of them

arrow.speed(0)
for i in range(1, minutes+1):

    arrow.circle(-250, i*6)

    arrow.right(90)

    if i % 5 == 0 and i % 15 == 0:
        arrow.forward(50)
        arrow.write(i/5, font=("Helvetica", 24, "normal"))
    elif i % 5 == 0:
        arrow.forward(25)
    
        if i ==5 or i == 10 or i == 20:
            arrow.penup()
            arrow.forward(20)
            arrow.pendown()
            arrow.write(i/5, font=("Helvetica", 24, "normal"))
        else:
            arrow.write(i/5, font=("Helvetica", 24, "normal"))
                 
    else:
        arrow.forward(10)

    arrow.setheading(0)
    arrow.penup()
    arrow.goto(home)
    arrow.pendown()


arrow.hideturtle()

# turning off animation
screen.tracer(0)

# creating digital clock title

digital_title = turtle.Turtle()
digital_title.teleport(-150, -350)
digital_title.write("Digital Clock", font=("Helvetica", 48, "bold"))
digital_title.forward(300)

digital_title.hideturtle()


# creating the digital clock background

digital = turtle.Turtle()

digital.teleport(-200, -400)

digital.color("black", "blue")
digital.begin_fill()


digital.forward(400)
digital.right(90)

digital.forward(80)
digital.right(90)

digital.forward(400)
digital.right(90)

digital.forward(80)
digital.right(90)
digital.end_fill()

digital.hideturtle()

# turtles used for the digital clock numbers
digital_second = turtle.Turtle()
digital_minute = turtle.Turtle()
digital_hour = turtle.Turtle()

for number in (digital_second, digital_minute, digital_hour):
    number.hideturtle()

screen.update()


# creating digital clock numbers
def drawing_digital_numbers():
    now = datetime.now()

    #second
    digital_second.clear()
    digital_second.teleport(40, -460)
    digital_second.write(f"{now.second:02d}", font=("Helvetica", 36, "bold"))

     #minute
    digital_minute.clear()
    digital_minute.teleport(-25, -460)
    digital_minute.write(f"{now.minute:02d}:", font=("Helvetica", 36, "bold"))

     #hour
    digital_hour.clear()
    digital_hour.teleport(-90, -460)
    digital_hour.write(f"{now.hour:02d}:", font=("Helvetica", 36, "bold"))

    screen.update()

#creating analog clock lines

#drawing second line

second = turtle.Turtle()
second.speed(0)
second.color("green")


now = datetime.now()


second_degree = 90 - now.second * 6

second.setheading(second_degree)
second.forward(250)

# drawing minute line

minute = turtle.Turtle()
minute.speed(0)
minute.color("yellow")


minute_degree = 90 - now.minute * 6

minute.setheading(minute_degree)
minute.forward(230)

#drawing hour line

hour = turtle.Turtle()
hour.speed(0)
hour.color("red")


hour_degree = 90 - now.hour * 30 - ( now.minute // 12) * 6

hour.setheading(hour_degree)
hour.forward(150)

# function that draws the analog lines
def draw_lines():

    now = datetime.now()

    seconds = now.second + now.microsecond / 1_000_000
    minutes = now.minute + seconds / 60
    hours = (now.hour % 12) + minutes / 60

    second.clear()
    second.penup()        
    second.home()
    second.pendown()
    second.setheading(90 - seconds * 6)
    second.forward(250)

    minute.clear()
    minute.penup()        
    minute.home()
    minute.pendown()
    minute.setheading(90 - minutes * 6)
    minute.forward(230)

    hour.clear()
    hour.penup()        
    hour.home()
    hour.pendown()
    hour.setheading(90 - hours * 30)
    hour.forward(150)

    screen.update()

# function to update both digital and analog
def update_clock():
    drawing_digital_numbers()
    draw_lines()

    #calling back the function 6 times a second
    screen.ontimer(update_clock, 167)

#calling the update function   
update_clock()

turtle.done()


