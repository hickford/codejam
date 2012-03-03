#!python
# http://code.google.com/codejam/contest/dashboard?c=1277486#s=p2
import sys
from optparse import OptionParser
usage = "usage: %prog input"
parser = OptionParser(usage=usage)
(options, args) = parser.parse_args()
if args:
    if args[0] == "-":
        f = sys.stdin
    else:
        f = open(args[0])
elif not sys.stdin.isatty():
    f = sys.stdin
else:
    parser.error("Need input from file or stdin")

import re
import string
vowels = "aeiou"
consonants = "".join([x for x in string.ascii_lowercase if x not in vowels])

syllable = "[%s]*[%s][%s]*" % (consonants,vowels,consonants)
#print syllable
word = "(?:%s)+" % syllable
#print word
multiword = "(?:%s){2,}" % syllable
pattern = r"(%s)(%s)(\1)" % (multiword,word)
#print pattern
T = int(f.readline())
for i in range(1,T+1):
    expression = f.readline().strip()
    result = re.search(pattern,expression)
    if result:
        spell = "".join(result.groups()) 
        #print spell
        print "Case #%d: Spell!" % i
    else:
        print "Case #%d: Nothing." % i
    