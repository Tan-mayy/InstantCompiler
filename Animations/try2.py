import turtle
import time 

def show_anim():
    while True:
        player.shape('circle')
        time.sleep(0.5)
        player.shape('triangle')
        time.sleep(0.5)
        

win = turtle.Screen()
win.title('Blink Turtle Blink')
win.bgcolor('black')

player = turtle.Turtle()
player.color('green')
player.shape('turtle')


show_anim()
print('hey')





win.mainloop