#hELLO GUYS TODAY WE WILL CODE OLYMPIC FLAG
# SO LETS BEGIN
#OPEN A NEW PY FILE
#FOLLOW MY STEPS
#Only import needed is turtle


#import turtle,   ( If you dont have turtle installed, pip install turtle through cmd)

from turtle import *
#name our turtle 
tommy = Turtle()
#set shape to turtle 
tommy.shape("turtle")
#the above step was not important, it was only for visual satisfaction 
#set pen size
tommy.pensize(6)
#set colors of rings in top row of olympic flag
firstcol = ("blue", "black", "red")
for i in range(3):
  tommy.penup()
  tommy.pencolor(firstcol[i]) #set the colors to turtle
  tommy.goto(i*110, 0)
  tommy.pendown()
  tommy.circle(50)
#set second row colours

secondcol = ("", "yellow", "", "green")
for i in range(1, 4,):
   tommy.penup()
   tommy.color(secondcol[i])
   tommy.goto(i*55, -50)
   tommy.pendown()
   tommy.circle(50)
   
# run the file 
#BINGoOoOOo
