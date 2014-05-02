#!python3
"""Round 1A 2014 Problem A. Charging Chaos
https://code.google.com/codejam/contest/2984486/dashboard
Shota the farmer has a problem. He has just moved into his newly built farmhouse, but it turns out that the outlets haven't been configured correctly for all of his devices. Being a modern farmer, Shota owns a large number of smartphones and laptops, and even owns a tablet for his favorite cow Wagyu to use. In total, he owns N different devices."""

def solve(N, L, devices, outlets):   
    devices = [int(x, 2) for x in devices]
    outlets = [int(x, 2) for x in outlets]

    possible_patterns = list()

    for i, outlet in enumerate(outlets):
        # try assigning devices[0] to ith outlet
        # that determines the flip pattern
        flip_pattern = devices[0] ^ outlet
        if set(x ^ flip_pattern for x in outlets) == set(devices):
            possible_patterns.append(flip_pattern)

    if possible_patterns:
        return min(bin(pattern).lstrip("0b").count("1") for pattern in possible_patterns)

    return "NOT POSSIBLE"

if __name__ == "__main__":
    import fileinput
    f = fileinput.input()

    T = int(f.readline())
    for case in range(1,T+1):
        N, L = [int(x) for x in f.readline().split()]
        outlets = f.readline().split()
        devices = f.readline().split()
        assert len(outlets) == len(devices) == N
        answer = solve(N, L, devices, outlets)
        print("Case #{0}: {1}".format(case, answer))


