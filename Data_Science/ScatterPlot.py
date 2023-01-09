from matplotlib import cm
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9]
y = [17,12,63,54,154,56,47,78,93]

plt.scatter(x,y, c=[1,2,3,4,5,6,7,8,9],cmap='Accent')
plt.show()