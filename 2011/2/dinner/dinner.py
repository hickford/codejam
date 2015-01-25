#!python3
"""Problem C. Expensive Dinner
http://code.google.com/codejam/contest/dashboard?c=1150486#s=p2

Your friends are all going to a restaurant for dinner tonight. They're all very good at math, but they're all very strange: your ath friend (starting from 1) will be unhappy unless the total cost of the meal is a positive integer, and is divisible by a.

Your friends enter the restaurant one at a time. As soon as someone enters the restaurant, if that person is unhappy then the group will call a waiter immediately.

As long as there is at least one unhappy person in the restaurant, one of those unhappy people will buy the lowest-cost item that will make him or her happy. This will continue until nobody in the restaurant is unhappy, and then the waiter will leave. Fortunately, the restaurant sells food at every integer price. See the explanation of the first test case for an example.

Your friends could choose to enter the restaurant in any order. After the waiter has been called, if there is more than one unhappy person in the restaurant, any one of those unhappy people could choose to buy something first. The way in which all of those choices are made could have an effect on how many times the group calls a waiter.

As the owner of the restaurant, you employ some very tired waiters. You want to calculate the spread of your friends: the difference between the maximum number of times they might call a waiter and the minimum number of times they might call a waiter."""
from codejamhelpers import kth_root, primes

def spread(N):
    if N == 1:
        return 0
    else:
        # most waiters = sum(greatest k such that p**k <= N over p a prime less than or equal to N)
        #              = pi(n) + pi(n**1/2) + pi(n**1/3) + pi(n**1/4) + ..              # by counting
        # fewest waiters = pi(n)
        answer = 1
        k = 2
        x = kth_root(N,k)
        while x >= 2:
            answer += primes.count(x)
            k += 1
            x = kth_root(N,k)
        return answer

if __name__ == "__main__":
    import fileinput
    f = fileinput.input()
    T = int(f.readline())
   
    for i in range(1,T+1):
        N = int(f.readline())
        answer = spread(N)
        print("Case #{0}: {1}".format(i,answer))

