import csv
import os
import datetime
import numpy as np

now = datetime.datetime.now()
filename = "sample%d" %now.year+"-%d" %now.month+"-%d" %now.day+"_%d" %now.hour+"_%d" %now.minute+"_%d" %now.second+ ".csv"
filename
os.system('cd /home/yujustin/Desktop/playground/CSV/rngCSV/ \ntouch'+filename)
#os.system('touch '+ filename)

#generates csv file with 1000 rows and 2 columns where first column is index
with open(filename, 'w') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    for x in range(0,50):
            y = np.random.randint(50, 75)
            spamwriter.writerow([x, y])
