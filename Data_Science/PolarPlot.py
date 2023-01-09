import matplotlib.pyplot as plt
import numpy as np

theta = np.arange((0,2*np.pi),0.01)
r = 2

for radian in theta:
    plt.polar(radian,r)
