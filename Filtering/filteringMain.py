import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from FIR import fir
filename = 'sample2020-10-8_22_53_45'
data = np.genfromtxt(filename+".csv" , delimiter=" ", names=["x", "y"])
data1 = np.zeros(0)

x = fir(6)
for i in data['y']:
    print('in: %f' % i)
    print('out: %f' % x.apply(i))
    data1 = np.append(data1, x.apply(i))
print(data1)
plt.plot(data['x'],data['y'], color = 'red', label='unfiltered')
plt.plot(data['x'],data1, label= 'filtered')
plt.legend(loc='best')
plt.title('simple FIR filter - 6 sample moving average')
plt.savefig(filename+"_filtered_data1.png")
