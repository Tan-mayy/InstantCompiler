import matplotlib.pyplot as plt

values = [12, 20, 35, 25, 8]
plt.pie(values, labels=['a','b','c','d','e'], explode=[0,0,0.033333,0,0])
plt.show()