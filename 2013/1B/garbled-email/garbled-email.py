#!python3
# https://code.google.com/codejam/contest/2434486/dashboard#s=p2 
""" Gagan just got an email from her friend Jorge. The email contains important information, but unfortunately it was corrupted when it was sent: all of the spaces are missing, and after the removal of the spaces, some of the letters have been changed to other letters! All Gagan has now is a string S of lower-case characters.

You know that the email was originally made out of words from the dictionary described below. You also know the letters were changed after the spaces were removed, and that the difference between the indices of any two letter changes is not less than 5. So for example, the string "code jam" could have become "codejam", "dodejbm", "zodejan" or "cidejab", but not "kodezam" (because the distance between the indices of the "k" change and the "z" change is only 4).

What is the minimum number of letters that could have been changed?"""

from string import ascii_lowercase
from datrie import Trie # pip install datrie
import os.path, sys

# restore trie, else download and make one
trie_path = 'trie.dump'
if os.path.exists(trie_path):
    trie = Trie.load(trie_path)
else:
    dict_path = "garbled_email_dictionary.txt"
    dict_url = "https://code.google.com/codejam/contest/static/garbled_email_dictionary.txt"
    if not os.path.exists(dict_path):
        from urllib.request import urlretrieve
        urlretrieve(dict_url, dict_path)

    with open(dict_path) as f:
        words = [line.strip() for line in f.readlines()]

    trie = Trie(ascii_lowercase)
    for word in words:
        trie[word] = True
    trie.save(trie_path)

class MinDict(dict):
    """Dictionary that only []overwrites values with smaller values"""
    def __setitem__(self, key, value):
        oldvalue = self.get(key, None)
        if oldvalue == None or value < oldvalue:
            dict.__setitem__(self, key, value)

def solve(email, min_gap = 5):
    # (cost, sentence) by (prefix, time allowed until next edit)
    costs = MinDict()
    costs["", 0] = (0, [])

    for i, x in enumerate(email):
        new_costs = MinDict()
        for (prefix, time), (cost, sentence) in costs.items():
            # try with letter as in email
            new_prefix = prefix + x
            new_time = max(0, time-1)
            new_cost = cost
            if trie.has_keys_with_prefix(new_prefix):
                new_costs[new_prefix, new_time] = (new_cost, sentence)
                if new_prefix in trie:
                    new_costs["", new_time] = (new_cost, sentence + [new_prefix])

            # try making edit (if allowed)
            if time > 0:
                continue
            new_cost = cost + 1
            for a in ascii_lowercase:
                if a == x:
                    # already considered above for cheaper
                    continue
                new_prefix = prefix + a
                new_time = min_gap - 1 # after 4 more letters, can make edit again
                if trie.has_keys_with_prefix(new_prefix):
                    new_costs[new_prefix, new_time] = (new_cost, sentence)
                    if new_prefix in trie:
                        new_costs["", new_time] = (new_cost, sentence + [new_prefix])
        
        costs = new_costs

    # ignore any solutions with incomplete final word
    complete_costs = [(cost, sentence) for (prefix, time), (cost, sentence) in costs.items() if prefix == ""]
    if not complete_costs:
        return "IMPOSSIBLE"
    cost, sentence = min(complete_costs, key = lambda pair: pair[0])    
    # print(" ".join(sentence), file = sys.stderr) # disappointingly boring!
    return cost

if __name__ == "__main__":
    import fileinput
    f = fileinput.input()
    T = int(f.readline())
    for case in range(1, T+1):
        email = f.readline().strip()
        answer = solve(email, 5)
        print("Case #%d: %s" % (case, answer))
