def f(x):
    a = abs(x)
    b = -2 * abs(x - 60)
    c = abs(x - 120)
    ans = (a + b + c)/4
    return ans



def counter(k, a=20, r=1000):
    memory = {(20, 0): f(20)}
    def g(x, n):
        if (x, n) in memory:
            return memory[(x, n)]

        ans = None
        if n == 0:
            ans = f(x)
        else:
            ans = f(x + k*g(x, n-1))

        memory[(x, n)] = ans
        return ans


    vals = set()
    for n in range(0, r):
        vals.add(g(a, n))

    #print(vals)
    return len(vals)


"""
def converge_test(k, a=20, r=1000, lim=10):
    count = counter(k, a, r)
    #print(k, count)
    if count > lim:
        return [False]
    else:
        return [True, '\t', count]
    


for i in range(0, 1000):
    #break
    k = i/100
    print(k, '\t', *converge_test(k))


#print(2, '\t', converge_test(2))
"""




try:
    file = open("data.txt", 'x')
except FileExistsError:
    file = open("data.txt", 'w')


"""
for i in range(0, 10_000):
    if (i % 100) == 0:
        print(i)
    k = i/1000
    count = counter(k)
    file.write(f"{k}\t{count}\n")
"""


#file.close()



for den in range(1, 100+1):
    print(den)
    for num in range(1, den):
        k = num/den
        count = counter(k)
        file.write(f"{count}\t")
    file.write('\n')
    


file.close()





























































































