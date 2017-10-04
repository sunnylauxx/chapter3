##Enhance your program above to also tell us what the drunk pirate’s heading
##is after he has finished stumbling around. (Assume he begins at heading 0).


import turtle 
wn = turtle.Screen()
alex = turtle.Turtle()
steps = [160, -43, 270, -97, -43, 200, -940, 17, -86]

for i in steps: 
    alex.left (i)
    alex.forward (100)
    
print(alex.heading())