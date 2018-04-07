import math
from math import sqrt, pi, sin, cos

# assume 2d

def shadow(rotation):
    return sqrt(2) * sin(rotation + pi/4)

assert abs(shadow(0) - 1) < 1e-12
assert abs(shadow(pi/4) - sqrt(2)) < 1e-12

def inverse(A):
    rotation = math.asin(A/sqrt(2)) - pi/4
    return rotation

T = int(input())
for case in range(1, T+1):
    A = float(input())
    rotation = inverse(A)
    
    print("Case #{}:".format(case))
    print("{} {} 0".format(sin(rotation)/2, cos(rotation)/2))
    print("{} {} 0".format(-cos(rotation)/2, sin(rotation)/2))
    print("0 0 0.5")

