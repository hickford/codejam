from random import randint

T = 100
print(T)

for case in range(T):
    N = randint(2, 500) if case < T-6 else 10**5
    print(N)
    W = [randint(1, 10**9) for i in range(N)]
    print(" ".join(map(str,W)))
