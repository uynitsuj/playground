import csv
numchar = ng = ngpriv = ngpub = nb = nbpriv = nbpub = 0

with open('marvel-wikia-data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        numchar += 1
        if (row['ALIGN'] == 'Good Characters'):
            ng += 1
        if (row['ALIGN'] == 'Good Characters' and row['ID'] == 'Secret Identity'):
            ngpriv += 1
        if (row['ALIGN'] == 'Good Characters' and (row['ID'] == 'Public Identity' or row['ID'] == 'No Dual Identity')):
            ngpub += 1
        if (row['ALIGN'] == 'Bad Characters'):
            nb += 1
        if (row['ALIGN'] == 'Bad Characters' and row['ID'] == 'Secret Identity'):
            nbpriv += 1
        if (row['ALIGN'] == 'Bad Characters' and (row['ID'] == 'Public Identity' or row['ID'] == 'No Dual Identity')):
            nbpub += 1
        # if row['']
        # print(row[])
print("Total: " + str(numchar))
print("Good Aligned: " + str(ng))
print("Good Aligned w/ Secret Identity: " + str(ngpriv))
print("Good Aligned w/ Public or No Dual Identity: " + str(ngpub))

print("Bad Aligned: " + str(nb))
print("Bad Aligned w/ Secret Identity: " + str(nbpriv))
print("Bad Aligned w/ Public or No Dual Identity: " + str(nbpub))
