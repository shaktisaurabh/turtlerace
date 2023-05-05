from turtle import Turtle,Screen 
import random
s=Screen()
s.setup(width=500,height=400)
y_axis=[-70,-40,-10,20,50,80]
colorsss=['red','yellow','orange','blue','purple','green','brown']
is_on=False
user_input=s.textinput(title="let's play a game",prompt="which colour do you bet on amongst red,yellow,orange,blue,purple,green,brown: ")#sends a bar and demands a user input and stores that in a vaariable
all_turt=[]
for i in range(0,6):
    new=Turtle()
    new.color(colorsss[i])#new turtle is made,color is inserted,pen is up so that a line isnot drawn
    new.penup()
    new.shape("turtle")
    new.goto(x=-250,y=y_axis[i])#x_axis is always end but y axis gets chosen
    all_turt.append(new)
# if user_input not in colorsss:
#     user_input=s.textinput(title="let's play a game",prompt="which colour do you bet on: ")
if user_input:#this means that if user_input variable exists only then is_on will be set true
      is_on=True

while is_on:#this will ensure that the for loop keeps running and turtles keep running until one of them reaches 230 distance across x-axis
    for k in all_turt:#for every instance of for loop,every turtle is moved ahead,their distance along x coordinate is checked and so is 
        #their pencolor and then a random distance gets alloted to each of them if if clause is verified as wrong
        if k.xcor()==230:
            is_on=False
            if k.pencolor()==user_input:
                print("you won")
            else:
                print(f"you lost,the turtle of {k.pencolor()} color won the race")
        sms=random.randint(0,10)
        k.forward(sms)
s.exitonclick()

        
    
