import sys
sys.setrecursionlimit(2000)



def f(x):
    a = abs(x)
    b = abs(x-60)
    c = abs(x-120)

    ans = a - 2*b + c
    ans /= 4

    return ans



memory = {}
def g(x, n, k):
    global memory
    
    if n == 0:
        memory[(x, n, k)] = 0
    if (x, n) not in memory:
        ans = f(x + k*g(x, n-1, k))
        memory[(x, n, k)] = 0

    return memory[(x, n, k)]



try:
    file = open("data.txt", 'x')
except FileExistsError:
    file = open("data.txt", 'w')


for K in range(0, 10_000):
    k = K/1_000
    values = set()
    
    for n in range(100):
        values.add(g(30, 1_000+n, k))
    print(values)

    file.write(f"{k}\t{len(values)}\n")
    
        

file.close()
