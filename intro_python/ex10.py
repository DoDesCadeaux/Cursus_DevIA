from random import randint
from ex8 import even_odd

nbs = []
for i in range(1, 7):
    nbs.append(randint(1, 6))
    
print(nbs)

print(even_odd())
