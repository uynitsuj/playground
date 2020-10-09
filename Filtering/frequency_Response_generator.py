import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from FIR import fir


M = 11
ind = []
for x in (range(0, 1000)):
    ind.append(x*0.001)

print ind

data1 = np.zeros(0)
d = fir(M)
for i in ind:
    data1 = np.append(data1, d.freq_resp(i))
    #print('in: %f' % i)
    #print('out: %f' % x.apply_sma(i))
#print(data1)
plt.plot(ind,data1, color = 'red', label='%d pt' % M)
plt.ylabel('Amplitude')
plt.xlabel('Frequency')
plt.legend(loc='best')
plt.title('FIR Filter Frequency Response')
plt.savefig("%d _freq_resp.png" % M)
