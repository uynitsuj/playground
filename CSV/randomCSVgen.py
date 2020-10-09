import csv
import numpy as np

#generates csv file with 1000 rows and 2 columns where first column is index
with open('sample.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    for x in range(0,50):
            y = np.random.randint(50, 75)
            spamwriter.writerow([x, y])
