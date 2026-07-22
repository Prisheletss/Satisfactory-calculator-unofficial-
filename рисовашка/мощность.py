def roof(x):
    if (x % 1) == 0: return int(x)
    else: return int(x) + 1



def count(power):
    n = (10*power)**(1/1.32)
    return roof(n)



def MinPower(Power):
    n = (10*power)**(1/1.32)
    n = roof(n - 0.5)
    return n/10
