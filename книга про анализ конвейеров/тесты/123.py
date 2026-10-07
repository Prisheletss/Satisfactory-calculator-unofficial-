def f(x):
    a = abs(x)
    b = -2 * abs(x-60)
    c = abs(x-120)
    ans = a + b + c
    ans /= 4
    return ans



def g(x, k):
    ans = 0
    
    for i in range(10_001):
        ans = f(k*ans + x)

    return ans


try:
    file = open("data.txt", 'x')
except FileExistsError:
    file = open("data.txt", 'w')


d = 10

for i in range(120*d + 1):
    num = g(i/d, 2)
    file.write(f"{num}\n")

file.close()
