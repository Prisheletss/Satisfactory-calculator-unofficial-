values = {(0, 0): 0}

def y_2(x, y):
    if (x, y) in values:
        return values[x, y]

    ans = None
    
    if y <= 120:
        if (x + y) <= 120:
            ans = y/4
        else:
            if (x + y) <= 180:
                ans = y/4
            else:
                if(2*x + y) <= 360:
                    ans = 90 - (x/2) - (y/4)
                else:
                    ans = 0
    else:
        if (x + y) <= 180:
            ans = (y/2) - 30
        else:
            if x <= 120:
                ans = 60 - (x/2)
            else:
                ans = 0

    values[(x, y)] = ans
    return ans




for k in range(1, 100):
    print(k)
    for x in range(1, k*180):
        for y in range(1, k*180):
            p = y_2(x/k, y/k)
            if p != 0:  
                if y_2(x/k, y/k + p)== 0:
                    print(x, y, p, k)

