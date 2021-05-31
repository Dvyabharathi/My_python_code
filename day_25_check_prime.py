import math

def is_prime(n):
    if n<2:
        return False
    limit = int(math.sqrt(n))
    for i in range(2, limit+1):
        if n%i==0:
            return False
    return True

T = int(input())
for x in range(T):
    n = int(input())
    res = is_prime(n)
    if res:
        print("Prime")
    else:
        print("Not prime")
