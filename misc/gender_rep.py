import numpy as np
import matplotlib.pyplot as plt
import csv

yearlist = []
fomrlist = []
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
            prevYr = row['Year']

font = {'family': 'sans-serif',
        'color':  'black',
        'weight': 'medium',
        'size': 19,
        }
yearlist = np.asarray(yearlist, dtype='float')
plt.plot(yearlist, fomrlist, linewidth=3, color='#FF81C0')
plt.xticks(rotation=70)
plt.ylabel('Female Percentage (%)', fontdict=font)
plt.xlabel('Year', fontdict=font)
plt.xlim(1945, 2013)
plt.show()
