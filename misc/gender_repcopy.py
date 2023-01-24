import numpy as np
import matplotlib.pyplot as plt
import csv

yearlist = []
fomrlist = []
mofrlist = []
fct = n = 0
prevYr = None

with open('marvel-wikia-data2.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Year'] != '':
            n += 1
            if row['SEX'] == 'Female Characters':
                fct += 1

            if row['Year'] != prevYr:
                yearlist.append(prevYr)
                fomrlist.append(fct/n*100)
                mofrlist.append(100-fct/n*100)
            prevYr = row['Year']

font = {'family': 'sans-serif',
        'color':  'black',
        'weight': 'medium',
        'size': 15,
        }
yearlist = np.asarray(yearlist, dtype='float')

plt.plot(yearlist, mofrlist, linewidth=2.6, color='b', linestyle=':')
plt.plot(yearlist, fomrlist, linewidth=2.6, color='#FF81C0', linestyle='--')
# plt.xticks(rotation=70)
plt.ylabel('Percentage (%)', fontdict=font)
plt.xlabel('Year', fontdict=font)
plt.xlim(1945, 2013)
plt.ylim(0, 100)
plt.legend(['Male', 'Female'], fontsize=10)
plt.show()
