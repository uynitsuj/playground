import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from FIR import fir
filename = 'data1'
#data = np.genfromtxt(filename+".csv" , delimiter=" ", names=["x", "y"])
data = np.genfromtxt(filename+".csv" , delimiter=" ", names=["y"])
data1 = np.zeros(0)
ind = []
for x in range(0,len(data)):
    ind.append(x)

x = fir(6)
for i in data['y']:
    #print('in: %f' % i)
    #print('out: %f' % x.apply(i))
    data1 = np.append(data1, x.apply_sma(i))
#print(data1)
plt.plot(ind,data['y'], color = 'red', label='unfiltered', linewidth=0.45)
plt.plot(ind,data1, label= 'filtered', linewidth=0.8)
plt.legend(loc='best')
plt.title('simple FIR filter - 6 sample moving average')
plt.savefig(filename+"_filtered_data1.png")

plt.close()

data1 = np.zeros(0)

x = fir(1000)
for i in data['y']:
    #print('in: %f' % i)
    #print('out: %f' % x.apply(i))
    data1 = np.append(data1, x.apply_sma(i))
#print(data1)
plt.plot(ind,data['y'], color = 'red', label='unfiltered', linewidth=0.45)
plt.plot(ind,data1, label= 'filtered', linewidth=0.8)
plt.legend(loc='best')
plt.title('simple FIR filter - 1000 sample moving average')
plt.savefig(filename+"_filtered_data2.png")
