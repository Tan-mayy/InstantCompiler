import turtle
import time

window = turtle.Screen()
window.title("My First Animation...")
window.bgcolor("black")

player = turtle.Turtle()
player.shape('arrow')
player.color('cyan')

while True:
    player.shape('arrow')
    time.sleep(0.4)
    player.shape('circle')
    time.sleep(0.4)
    player.shape('square')
    time.sleep(0.4)
    player.color('red')
    player.shape('turtle')
    player.color('yellow')
    time.sleep(0.4)
    player.shape('triangle')
    time.sleep(0.4)






window.mainloop()
