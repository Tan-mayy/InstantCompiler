from re import X
import matplotlib.pyplot as plt

# Graph of x = y^2
x1 = [1, 4, 9, 16, 25, 36, 49]
y1 = [1, 2, 3, 4, 5, 6, 7]

# Graph for y = X
x2 = [1,2,3,4,5,6,7]
y2 = [1,2,3,4,5,6,7]

plt.plot(x1,y1,'r')
plt.plot(x2,y2,'y')

plt.title(' Analysing Multiple Graphs under a Single Graph')
plt.legend('x = y^2', 'x = y')
plt.xlabel('x- axis')
plt.ylabel('y- axis')
plt.show()