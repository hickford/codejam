#!python3
# https://code.google.com/codejam/contest/2434486/dashboard#s=p2

from string import ascii_lowercase
import datrie

with open('garbled_email_dictionary.txt') as f:
    words = [line.strip() for line in f.readlines()]

# trie = marisa_trie.Trie

trie = datrie.Trie(ascii_lowercase)
for word in words:
    trie[word] = True

class MinDict(dict):
    def __setitem__(self, key, value):
        oldvalue = self.get(key, None)
        if oldvalue == None or value < oldvalue:
            dict.__setitem__(self, key, value)

def solve(email):
    # costs by (prefix, time allowed until next edit)
    costs = MinDict()
    costs["", 0] = 0

    for i, x in enumerate(email):
        new_costs = MinDict()
        for (prefix, time), cost in costs.items():
            # try with letter from garbled email
            new_prefix = prefix + x
            new_time = max(0, time-1)
            new_cost = cost
            if trie.has_keys_with_prefix(new_prefix):
                new_costs[new_prefix, new_time] = new_cost
                if new_prefix in trie:
                    new_costs["", new_time] = new_cost

            # try making edit (if allowed)
            if time > 0:
                continue
            new_cost = cost + 1
            for a in ascii_lowercase:
                if a == x:
                    # already considered above
                    continue
                new_prefix = prefix + a
                new_time = 4
                if trie.has_keys_with_prefix(new_prefix):
                    new_costs[new_prefix, new_time] = new_cost
                    if new_prefix in trie:
                        new_costs["", new_time] = new_cost
        
        costs = new_costs

    return min(cost for (prefix, time), cost in costs.items() if prefix == "")

if __name__ == "__main__":
    import fileinput
    f = fileinput.input()
    T = int(f.readline())
    for case in range(1, T+1):
        email = f.readline().strip()
        answer = solve(email)
        print("Case #%d: %s" % (case, answer))
