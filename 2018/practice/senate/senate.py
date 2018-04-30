from string import ascii_uppercase
T = int(input())
for case in range(1, T+1):
    N = int(input())
    parties = [int(x) for x in input().split()]
    solution = list()
    while sum(parties) > 0:
        remaining = [i for i in range(N) if parties[i] > 0]
        size_of_largest = max(parties)
        if len(remaining) == 2 and sum(parties) == 2*size_of_largest:
            a, b = remaining
            solution.append(ascii_uppercase[a] + ascii_uppercase[b])
            parties[a] -= 1
            parties[b] -= 1
        else:
            a = max(range(N), key=lambda i:parties[i])
            parties[a] -= 1
            solution.append(ascii_uppercase[a])
            
    print("Case #{}: {}".format(case, " ".join(solution)))