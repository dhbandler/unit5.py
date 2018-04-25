#Daniel Bandler
#4/25/18
#warmup13.py makes list of random numbers and does things with them

from random import randint
L = []
for i in range(1,21):
    L.append(randint(1,101))

print(sum(L))
print(min(L))
print(max(L))
