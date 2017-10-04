import turtle           
wn = turtle.Screen()
wn.title("A face of a clock")
wn.bgcolor("lightgreen")
   
alex = turtle.Turtle()
alex.pensize(3)
alex.speed(0)
alex.shape("turtle")
alex.color("blue")
  
for i in range(12):
    alex.penup()
    alex.forward(80)
    alex.pendown()
    alex.forward(10)
    alex.penup()
    alex.forward(30)
    alex.stamp()
    alex.backward(120)
    alex.right(30)
 
 
          
  