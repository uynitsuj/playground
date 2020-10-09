import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data = np.genfromtxt("sample.csv" , delimiter=" ", names=["x", "y"])

plt.plot(data['x'],data['y'])
plt.savefig("sample.png")
