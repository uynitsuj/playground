import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
filename = 'eecs200_020921_021235.txt'
data = np.genfromtxt(filename, delimiter=" ", names=["x", "y"])
plt.plot(data['x'],data['y'])
plt.savefig(filename+".png")
