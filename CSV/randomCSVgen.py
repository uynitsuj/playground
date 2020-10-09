import csv
import os
import subprocess
import datetime
import numpy as np

#touches new file in playground directory
now = datetime.datetime.now()
filename = "sample%d" %now.year+"-%d" %now.month+"-%d" %now.day+"_%d" %now.hour+"_%d" %now.minute+"_%d" %now.second+ ".csv"
filename
subprocess.call('touch '+filename, shell=True)

#generates csv file with 50 rows and 2 columns where first column is index
with open(filename, 'w') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    for x in range(0,50):
            y = np.random.randint(50, 75)
            spamwriter.writerow([x, y])
