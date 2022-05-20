odds=[]
for i in range(0,100):
    if i%2!=0:
        odds.append(i)

for n in odds:
    print(odds[:odds.index(n)])
    print(sum(odds[:odds.index(n)]))
