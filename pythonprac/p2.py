# ABCDE*4=EDCBA
for i in range(10000, 100000):
    #i = 21978
    n = [(i//10000) % 10, (i//1000) % 10, (i//100) % 10, (i//10) % 10, i % 10]
    print(n)

    newn = n[0]+n[1]*10+n[2]*100+n[3]*1000+n[4]*10000
    newn = int(newn)
    print(newn)
    if (newn == 4*i):
        print(i)
        break

    # print(n)
