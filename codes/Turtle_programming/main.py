# draw square in Python Turtle
import turtle
  
t = turtle.Turtle()
 
s = int(input("Enter the length of the side of the Square: "))
 
# drawing first side
t.forward(s) 
t.left(90) 
 
# drawing second side
t.forward(s) 
t.left(90)
 
# drawing third side
t.forward(s) 
t.left(90) 
 
# drawing fourth side
t.forward(s)
t.left(90) 