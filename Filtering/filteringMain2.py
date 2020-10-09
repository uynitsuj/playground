import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from FIR import fir
filename = 'sample2020-10-9_1_12_23'
data = np.genfromtxt(filename+".csv" , delimiter=" ", names=["x", "y"])
data1 = np.zeros(0)

x = fir(6)
for i in data['y']:
    print('in: %f' % i)
    print('out: %f' % x.apply(i))
    data1 = np.append(data1, x.apply(i))
print(data1)
plt.plot(data['x'],data['y'], color = 'red', label='unfiltered', linewidth=0.45)
plt.plot(data['x'],data1, label= 'filtered', linewidth=0.8)
plt.legend(loc='best')
plt.title('simple FIR filter - 6 sample moving average')
plt.savefig(filename+"_filtered_data1.png")

plt.close()

data1 = np.zeros(0)

x = fir(15)
for i in data['y']:
    print('in: %f' % i)
    print('out: %f' % x.apply(i))
    data1 = np.append(data1, x.apply(i))
print(data1)
plt.plot(data['x'],data['y'], color = 'red', label='unfiltered', linewidth=0.45)
plt.plot(data['x'],data1, label= 'filtered', linewidth=0.8)
plt.legend(loc='best')
plt.title('simple FIR filter - 15 sample moving average')
plt.savefig(filename+"_filtered_data2.png")
