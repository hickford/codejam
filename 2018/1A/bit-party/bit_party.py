# https://codejam.withgoogle.com/2018/challenges/0000000000007883/dashboard/000000000002fff6
"""Bit Party
These days, robots can drive cars, but can they throw a good party? The Code Jam team's research into this topic is still at an early stage. We just deployed R robot shoppers to our local supermarket to buy party supplies for our World Finals in Toronto, but their first-order model of a Canadian party was very simple: they just bought B "bits" (a bit being a small donut-like treat found in the area). We will work on improving their AI later, but for now, we want to help them purchase all of those bits as quickly as possible."""

import fileinput
from sys import stderr
f = fileinput.input()
def input():
    return f.readline()

T = int(input())
for case in range(1, T+1):
    R, B, C = [int(x) for x in input().split()] # numbers of robot shoppers, bits, and cashiers
    cashiers = [[int(x) for x in input().split()] for i in range(C)]
    # cashiers.sort(key=lambda x: x[0])
    maxes, scan_times, payment_times = zip(*cashiers)

    bits_per_cashier = [0 for i in range(C)]
    cashiers = sorted(range(C), key=lambda i: maxes[i])
    for i in cashiers[-R:]:
        bits_per_cashier[i] = maxes[i]
        if sum(bits_per_cashier) > B:
            bits_per_cashier[i] -= sum(bits_per_cashier) - B
            break
    assert sum(bits_per_cashier) == B
    
    def time(i, bits=None):
        if bits == None:
            bits = bits_per_cashier[i]
        if bits == 0:
            return 0
        return bits * scan_times[i] + payment_times[i]

    found_improvement = True
    while(found_improvement):
        limiting = max(range(C), key=time)
        limit = time(limiting)
        limiting_load = bits_per_cashier[limiting]
        # print(bits_per_cashier, limit)
        robots_used = len([b for b in bits_per_cashier if b])
        found_improvement = False
        for i in range(C):
            if i == limiting:
                continue
            current = bits_per_cashier[i]
            # try swapping completely
            if current + limiting_load <= maxes[i] and time(i, current+limiting_load) < limit:
                bits_per_cashier[limiting] = 0
                bits_per_cashier[i] += limiting_load
                found_improvement = True
                break

            # try incrementing just one
            available = current or robots_used < R
            if available and current < maxes[i] and time(i, current+1) < limit:
                bits_per_cashier[limiting] -= 1
                bits_per_cashier[i] += 1
                found_improvement = True
                break

    print("Case {}: {}".format(case, limit))


