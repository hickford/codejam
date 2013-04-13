#!python
"https://code.google.com/codejam/contest/2270488/dashboard#s=p2"
from __future__ import division
import string, itertools, fileinput, bisect, sys

def is_palindrome(n):
    s = str(n)
    return s == reverse(s)
    
def reverse(s):
    return "".join(reversed(s))

def nth_root(N,k):
    """Return greatest integer x such that x**k <= N"""
    x = int(N**(1/k))       
    while (x+1)**k <= N:
        x += 1
    while x**k > N:
        x -= 1
    return x
    
small_palindromes = set()

max_length = 7

products = itertools.product(string.digits,repeat=(max_length+1)//2)
products.next()

for p in products:
    n = int("".join(p))
    half = str(n)
    
    candidates = [n, half+reverse(half), half + reverse(half[:-1])]
    for x in candidates:
        if is_palindrome(x):
            small_palindromes.add(int(x))
    
small_palindromes = sorted(small_palindromes)

# palindromes, 1 <= n < 10**max_length whose squares are palindromes
fas_roots = list()
fas = list()
for n in small_palindromes:
    square = n**2
    if is_palindrome(square):
        fas_roots.append(n)
        fas.append(square)
       
print >> sys.stderr, fas_roots
print >> sys.stderr, fas

f = fileinput.input()
T = int(f.readline())

def solve(A,B):
    return bisect.bisect_right(fas,B) - bisect.bisect_left(fas, A)

for case in range(1,T+1):
    A,B = [int(x) for x in f.readline().split()]

    answer = solve(A,B)
    print "Case #%d: %d" % (case, answer)