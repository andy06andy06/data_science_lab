import math

def frac(n):
    r = 1
    if n==0 or n==1:
        return 1
    else:
        for n in range(1, n+1):
            r *= n
    return r

def estimate_pi():
    k = 0; sum = 0; last_term = 0
    while last_term < 1e-15:
        last_term = (2*pow(2, 0.5)/9801*frac(4*k)
                     *(1103 + 26390*k)/frac(k)/pow(396, 4*k))
        k += 1
        sum += last_term
    print(1/sum)

estimate_pi()
print(math.pi)
        

