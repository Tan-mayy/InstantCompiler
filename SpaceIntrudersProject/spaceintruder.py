import math
import random
import turtle
import os
# from playsound import playsound


# Main Screen
window = turtle.Screen()
window.bgcolor("black")
window.title("Space Intruder")
window.bgpic(os.path.expanduser("~/Desktop/project/bgspace.gif"))
window.tracer(0)  #Don't update the window


# Register the shapes ....
window.addshape(os.path.expanduser("~/Desktop/project/ship2.gif"))
window.addshape(os.path.expanduser("~/Desktop/project/invader.gif"))
window.addshape(os.path.expanduser("~/Desktop/project/muzzle.gif"))
# turtle.register_shape(os.path.expanduser("~/Desktop/project/intruder23.gif"))

 
# For Borders
pen = turtle.Turtle()
pen.color('white')
pen.speed(0)
pen.up()
pen.setposition(-300,-300)
pen.pensize(3)
pen.down()

for i in range(4):
    pen.forward(600)
    pen.left(90)
pen.hideturtle()

# Creating our player.........
hero = turtle.Turtle()
hero.color('light blue') 
hero.shape(os.path.expanduser("~/Desktop/project/ship2.gif"))
hero.penup()
hero.speed(0)
hero.goto(0,-250)
hero.left(90)

# Setting score to zero.....
score = 0

# Creating score for the player...
score_pen = turtle.Turtle()
score_pen.penup()
score_pen.color('white')
score_pen.speed(0)
score_pen.setposition(-285,275)
scorestring = "Score: {}" .format(score)
score_pen.write(scorestring, False, align= "Left" , font = ("Arial", 14 , "normal"))
score_pen.hideturtle()

# Creating a bullet for enemies....
bullet = turtle.Turtle()
bullet.color('white')
bullet.shape(os.path.expanduser("~/Desktop/project/muzzle.gif"))
bullet.shapesize(0.5,0.5)
bullet.penup()
bullet.hideturtle()

bulletspeed = 2

# Defining state of bullet
# 1. Ready - When the player is ready to fire 
# 2, Fire - Fires the bullet

bulletstate = "Ready"

# Moving the player left and right.........
hero.speed = 0

# Choose the number of inruders...
no_of_intruder = 13

# Creating a list...
intruders = []

# Adding enemies to the list...
for i in range(no_of_intruder):
    intruders.append(turtle.Turtle())

for intruder in intruders:
    intruder.speed(0)
    intruder.penup()
    intruder.shape(os.path.expanduser("~/Desktop/project/invader.gif"))
    intruder.color('red')
    intruder.setposition(0,280)
    intruder.right(90)
    x = random.randint(-200,200)
    y = random.randint(130,270)
    intruder.setposition(x,y)

intruder_speed = 0.1

def move_left():
    hero.speed = -0.8
    
def move_right():
    hero.speed = 0.8

def move_hero():
    x = hero.xcor()
    if x < -250:
        x = -250
        hero.setx(x)
    x += hero.speed
    hero.setx(x)
    
    if x > 250:
        x -= hero.speed
        hero.setx(x)


# Firing the bullet....
def fire_bullet():

# Defining bullet state global because it'll change with funtion call
    global bulletstate
    if bulletstate == "Ready":
        # Creating sound...
        # playsound('E:\Py Codes\SpaceIntrudersProject\Space Invaders_laser.wav')
        bulletstate = "fire"

        x = hero.xcor()
        y = hero.ycor() + 20
        bullet.setposition(x,y)
        bullet.showturtle()

def IsCollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 10:
        return True
    else :
        return False    


# Assigning Keyboard Bindings to move the player...
window.listen()
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")
window.onkeypress(fire_bullet, 'space')





# Main Game Loop....
while True:

    window.update()
    

    move_hero()

    # playsound('E:\Py Codes\SpaceIntrudersProject\earth.wav')

    for intruder in intruders :
# Move right 
        x = intruder.xcor()
        x += intruder_speed
        intruder.setx(x)

# Moving down as it touches the boundry...
        if x > 260:
            # Move all down...
            for i in intruders:
                y = i.ycor()
                y -= 30
                i.sety(y)
                x += intruder_speed
            # Direction reversing    
            intruder_speed *= -1
           
        
    
        if x < -260:
            # Moving them down...
            for i in intruders:
                y = i.ycor()
                y -= 30
                i.sety(y)
                x += intruder_speed
            # Direction...    
            intruder_speed *= -1

# Checking collision between the enemy and bullet......
        if IsCollision(bullet,intruder) == True:
            

            # Reset the bullet......
            bullet.hideturtle()
            bullet.state = "Ready"
            bullet.setposition(0,-400)        

            # Intruder reset...
            x = random.randint(-200,200)
            y = random.randint(100,240)
            intruder.setposition(x,y)

            # Reset the score...
            score += 100
            scorestring = "Score: {}" .format(score)
            score_pen.clear()
            score_pen.write(scorestring, False, align= "Left" , font = ("Arial", 14 , "normal"))
            # playsound('E:\Py Codes\SpaceIntrudersProject\Space Invaders_laser.wav')
        
# Checking collision between hero and intruder......
        if IsCollision(hero, intruder) == True:
            # playsound('E:\Py Codes\SpaceIntrudersProject\explode.wav')
            hero.hideturtle()
            intruder.hideturtle()
            print(":::::  Game Over  :::::")
            break
            

# Moving the bullet...
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

# Checking bullet had reached top....
    if bullet.ycor() > 260:
        bullet.hideturtle()
        bulletstate = "Ready"













window.mainloop()