from turtle import color
import matplotlib.pyplot as plt

x = [10,20,25,56,23]
y = [0.33,0.5,0.6,0.9,1.4]

plt.bar(x,y, color= 'r', width=2)
plt.show()