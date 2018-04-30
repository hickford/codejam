#The first line of the input gives the number of test cases, T. T test cases follow. Each begins with one line with an integer M: the number of metals known in the world. Then there are M more lines with two integers Ri1 and Ri2 each; the i-th of these lines indicates that you can create one gram of metal i by destroying one gram of metal Ri1 and one gram of metal Ri2. Finally, there is one line with M integers G1, G2, ..., GM; Gi is the number of grams of metal i in the treasury. Lead is metal 1.

# The first line of the input gives the number of test cases, T. T test cases follow. Each begins with one line containing one integer S: the number of road signs. Then, S more lines follow. The i-th of these lines represents the i-th sign (in west-to-east order), and contains three integers Di, Ai, and Bi: the sign's distance (in kilometers) east of Signfield, the number on its west side, and the number on its east side.

import fileinput
from sys import stderr
f = fileinput.input()
def input():
    return f.readline()

T = int(input())
for case in range(1, T+1):
    M = int(input())
    ingredients = [[int(x) for x in input().split()] for _ in range(M)]
    treasury = [int(x) for x in input().split()]
    assert len(treasury) == M

    treasure_total = sum(treasury)

    def possible(lead):
        inventory = [0] * M
        inventory[0] = lead
        while True:
            if sum(inventory) > treasure_total:
                return False
            for i in range(M):
                if inventory[i] > treasury[i]:
                    surplus = inventory[i] - treasury[i]
                    inventory[i] -= surplus
                    for ingredient in ingredients[i]:
                        inventory[ingredient-1] += surplus
                    break
            else:
                return True

    upper = 1
    while possible(upper):
        upper *= 2

    lower = 0
    while upper > lower+1:
        mid = (upper + lower) // 2
        if possible(mid):
            lower = mid
        else:
            upper = mid

    solution = lower
    assert possible(solution) and not possible(solution + 1)

    print("Case #{}: {}".format(case, solution))




