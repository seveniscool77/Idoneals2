import time




def count(start=0, step=1):
    n = start
    while True:
        yield n
        n += step

        
def triple_generator():
    for x in count(start=3):
        for y in range(2, x):
            for z in range(1, y):
                yield (x, y, z)
triple = triple_generator()



N = int(input('name any N: '))
idoneal = []
not_idoneal = set()
triplets_checked = set()

start = time.time()

for n in range(1, N+1):
    if n in triplets_checked:
        pass
    else:
        next_triple = next(triple)
        calc = next_triple[0]*(next_triple[1]+next_triple[2]) + next_triple[1]*next_triple[2]
        not_idoneal.add(calc)
        triplets_checked.add(next_triple)
        while max(next_triple) <= (n+1)//3:
            if calc == n:
                not_idoneal.add(n)
                break
            next_triple = next(triple)
            calc = next_triple[0]*(next_triple[1]+next_triple[2]) + next_triple[1]*next_triple[2]
            not_idoneal.add(calc)
            triplets_checked.add(next_triple)
        else:
            if n not in not_idoneal:
                idoneal.append(n)

print(idoneal)
print(time.time() - start)

