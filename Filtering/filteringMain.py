import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from FIR import fir
from IIR import iir

filename = 'data2'
data = np.genfromtxt(filename+".csv" , delimiter=" ", names=["y"])
ind = []
for x in range(0,len(data)):
    ind.append(x)
data1 = np.zeros(0)
samples = 6
x = fir(samples)
for i in data['y']:
    data1 = np.append(data1, x.apply_sma(i))
    #print('in: %f' % i)
    #print('out: %f' % x.apply_sma(i))
#print(data1)
plt.plot(ind,data['y'], color = 'red', label='unfiltered')
plt.plot(ind,data1, label= 'filtered')
plt.legend(loc='best')
plt.title('simple FIR filter - %d sample moving average' % samples)
plt.savefig(filename+"_filtered_datafir1.png")

plt.close()

data2 = np.zeros(0)
x = iir(2,0.5,'lowpass',design='butter')


for i in data['y']:
    data2 = np.append(data2, x.apply(i))
    #print('in: %f' % i)
    #print('out: %f' % x.apply_sma(i))
#print(data1)
plt.plot(ind,data['y'], color = 'red', label='unfiltered')
plt.plot(ind,data2, label= 'filtered')
plt.legend(loc='best')
plt.title('IIR filter')
plt.savefig(filename+"_filtered_data_iir1.png")
