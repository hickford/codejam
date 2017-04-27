# https://code.google.com/codejam/contest/5304486/dashboard#s=p1
"""You've discovered it: the ultimate recipe for ratatouille, the famous French dish! You know which ingredients to use, and how many grams of each one to use, in order to make one serving of ratatouille. But you believe that anyone can cook, and so you want to share the recipe with the world... and make some money in the process!

You have ordered some ingredient packages that are easy to ship. Each package contains some amount of one ingredient; different packages may have different amounts even if they contain the same ingredient. For convenience, you ordered the same number of packages of each ingredient.

You would like to use these packages to form as many ratatouille kits as possible to send to customers. A kit consists of exactly one package of each ingredient, and a label with the integer number of servings of ratatouille that the kit makes. Since you do not want to shortchange customers or waste food, each package must contain between 90 and 110 percent (inclusive) of the amount of that ingredient that is actually needed to make the number of servings of ratatouille on the kit's label.

For example, suppose that one serving of ratatouille takes 500 g of tomato and 300 g of onion. Suppose that you have a 900 g package of tomato and a 660 g package of onion. You could form these into a kit that makes two servings of ratatouille. To make two servings, 1000 g of tomato and 600 g of onion are required. Since the 900 g of tomato you have is within [90, 110]% of the 1000 g of tomato required, and the 660 g of onion you have is within [90, 110]% of the 600 g of onion required, this is acceptable. However, you could not say that the kit makes one or three servings of ratatouille, nor could you say that it makes 1.999 servings (the number of servings must be an integer).

Note that there are some sets of packages that could never form a kit. Continuing with our recipe above, if you have a 1500 g package of tomato and an 809 g package of onion, for example, there is no amount of servings that you can make. Three servings would take 1500 g of tomato and 900 g of onion, and the amount of onion is not within the [90, 110]% range. No other integer amount of servings works, either.

You want to share your recipe with as many customers as possible, so you want to produce the maximum number of valid kits. (Of course, each package can be used in at most one kit.) What is the largest number of kits that you can form? Note that you are not required to maximize the total number of servings of ratatouille formed."""

from math import floor, ceil

def suitable(potential_kit, recipe, servings):
    return all(servings * recipe[i] * 0.9 <= potential_kit[i] <= servings * recipe[i] * 1.1 for i in range(len(recipe)))

import fileinput
f = fileinput.input()

T = int(f.readline())
for case in range(1, T+1):
    N, P = [int(x) for x in f.readline().split()]
    recipe = [int(x) for x in f.readline().split()]
    assert len(recipe) == N

    packages_by_ingredient = list()
    for i in range(N):
        packages_by_ingredient.append([int(x) for x in f.readline().split()])
        assert len(packages_by_ingredient[i]) == P
        packages_by_ingredient[i].sort()

    kits = list()
    while all(packages_by_ingredient):
        # package with largest multiple
        i = max(range(N), key=lambda i: packages_by_ingredient[i][-1] / recipe[i])
        potential_kit = [p[-1] for p in packages_by_ingredient]
        lower_bound_for_servings = ceil(potential_kit[i] / recipe[i] / 1.1)
        if suitable(potential_kit, recipe, lower_bound_for_servings):
            kits.append(potential_kit)
            for p in packages_by_ingredient:
                p.pop()
        else:
            packages_by_ingredient[i].pop()

    solution = len(kits)
    print(f"Case #{case}: {solution}")
