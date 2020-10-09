import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
filename = 'sample2020-10-9_1_12_23.csv'
data = np.genfromtxt(filename, delimiter=" ", names=["x", "y"])
plt.plot(data['x'],data['y'])
plt.savefig(filename+".png")
