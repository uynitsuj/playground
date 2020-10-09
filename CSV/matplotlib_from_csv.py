import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
filename = 'sample2020-10-8_22_53_45'
data = np.genfromtxt(filename+".csv" , delimiter=" ", names=["x", "y"])

plt.plot(data['x'],data['y'])
plt.savefig(filename+".png")
