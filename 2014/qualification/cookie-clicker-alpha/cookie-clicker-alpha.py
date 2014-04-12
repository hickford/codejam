#!python3
"""Google Code Jam Qualification Round 2014 Problem B. Cookie Clicker Alpha
https://code.google.com/codejam/contest/2974486/dashboard#s=p1
Cookie Clicker is a Javascript game by Orteil, where players click on a picture of a giant cookie. Clicking on the giant cookie gives them cookies. They can spend those cookies to buy buildings. Those buildings help them get even more cookies. Like this problem, the game is very cookie-focused. This problem has a similar idea, but it does not assume you have played Cookie Clicker. Please don't go play it now: it might be a long time before you come back.

In this problem, you start with 0 cookies. You gain cookies at a rate of 2 cookies per second, by clicking on a giant cookie. Any time you have at least C cookies, you can buy a cookie farm. Every time you buy a cookie farm, it costs you C cookies and gives you an extra F cookies per second.

Once you have X cookies that you haven't spent on farms, you win! Figure out how long it will take you to win if you use the best possible strategy."""

# Observe that any strategy in which a farm is bought when have strictly more than C cookies can be improved by buying that farm earlier. So consider only strategy in which buy n farms, each as soon as possible."""

def solve(C, F, X):
    def f(n):
        """Time taken if build n farms, all as soon as possible."""
        return sum(C/(2+i*F) for i in range(n)) + X / (2+n*F)
    best_n = binary_creep(f)
    return f(best_n)

def powers_of_two():
    n = 1
    while True:
        yield n
        n *= 2

def binary_creep(f):
    # minimise convex function f over integers n . Return minimising n*
    for n in powers_of_two():
        if f(n) >= f(n//2):
            break
            
    upper = n
    lower = n//4

    while upper > lower + 1:
        upper_third = (lower + 2*upper)//3
        lower_third = max((2*lower + upper)//3, lower + 1)
        if f(upper_third) >= f(lower_third):
            upper = upper_third
        else:
            lower = lower_third

    n_best = lower if f(lower) <= f(upper) else upper

    return n_best

if __name__ == "__main__":
    """The first line of the input gives the number of test cases, T. T lines follow. Each line contains three space-separated real-valued numbers: C, F and X, whose meanings are described earlier in the problem statement.

    C, F and X will each consist of at least 1 digit followed by 1 decimal point followed by from 1 to 5 digits. There will be no leading zeroes."""
    import fileinput
    f = fileinput.input()

    T = int(f.readline())
    for case in range(1,T+1):
        C, F, X = [float(x) for x in f.readline().split()]
        answer = solve(C, F, X)
        print("Case #{0}: {1}".format(case, answer))



