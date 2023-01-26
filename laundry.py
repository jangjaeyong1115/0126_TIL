import sys
T = int(sys.stdin.readline())

for i in range(T):
    charge = int(sys.stdin.readline())
    
    q = charge // 25
    charge %= 25

    d = charge // 10
    charge %= 10

    n = charge // 5
    charge %= 5

    p = charge
    print(q,d,n,p)