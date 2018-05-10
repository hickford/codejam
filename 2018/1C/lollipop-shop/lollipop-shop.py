# https://codejam.withgoogle.com/2018/challenges/0000000000007765/dashboard/000000000003e068
"""You own a lollipop shop. At the start of the day, you make N lollipops, each of a single unique flavor, like huckleberry, cherry or lime. N customers come into the shop during the day, one at a time. Each customer gives you a list of which of your lollipop flavors they like. You can sell them one lollipop of any of those flavors, as long as you have not already sold someone else the same flavor earlier in the day (since there is only one lollipop of each flavor). If none of the flavors they like are still available, you cannot sell them a lollipop, and they leave your shop disappointed.

You do not know what each customer's flavor preferences are going to be until they arrive. Each customer decides if they like or dislike each flavor randomly, independently of whether they like any other flavor, or what flavors anyone else likes. However, your market studies have shown that some flavors may have a higher probability of being liked in general! For example, the lime flavor might have a 10% chance of being liked by any particular customer, whereas that chance might be 1% for the cherry flavor. These values are always chosen independently and uniformly at random from the interval [0.005, 0.1].

Obviously, you want to sell lollipops to as many of the N customers as possible! But, since you do not know what flavors your customers will ask for ahead of time, you cannot always make an optimal decision - sometimes you might sell a customer one flavor, and then later wish you had sold them another.

Suppose that you somehow knew all the customers' preferences in advance and could plan ahead; then there is some maximum number M of lollipops that you could possibly sell. You do not know the customers' preferences in advance, but we require you to sell a number of lollipops that is at least 90% of M for each input case."""

from math import sqrt

T = int(input())
for case in range(1, T+1):
    N = int(input())
    assert N >= 1

    remaining = set(range(N))
    seen = [0] * N

    for customer in range(N):
        D, *prefs = [int(x) for x in input().split()]
        assert len(prefs) == D
        feasible = set(prefs) & remaining
        if feasible:
            novel_flavours = [i for i in feasible if not seen[i]]
            least_popular_flavour = min(feasible, key=lambda i: seen[i])
            choice = least_popular_flavour
            remaining.remove(choice)
        else:
            choice = -1
        print(choice)
        for flavour in prefs:
            seen[flavour] += 1
