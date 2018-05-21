from itertools import accumulate

T = int(input())
for case in range(1, T+1):
    R, B = [int(x) for x in input().split()]

    jugglers = 0
    diagonal = 1
    while diagonal <= R + B:
        for r in range(0, R+1):
            b = diagonal - r
            if r <= R and b <= B:
                jugglers += 1
                R -= r
                B -= b
        diagonal += 1

    solution = jugglers
    print("Case #{}: {}".format(case, solution))
