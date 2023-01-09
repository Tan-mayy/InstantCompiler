import turtle
import time

win = turtle.Screen()
win.title('Dice ')
win.bgcolor('black')

win.register_shape('C:\Program Files\dice.png')

dice = turtle.Turtle()
dice.shape('dice.png')
dice.color('white')


win.mainloop