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

def solve(email):
    hypotheticals = [("", 0, 0)]    # prefix, cost, time until allowed next edit
    for i, x in enumerate(email):
        new_hypotheticals = []
        for (prefix, cost, time) in hypotheticals:
            # try with letter from garbled email
            new_prefix = prefix + x
            new_time = max(0, time-1)
            new_cost = cost
            if trie.has_keys_with_prefix(new_prefix):
                new_hypotheticals.append((new_prefix, new_cost, new_time))
                if new_prefix in trie:
                    # print(new_prefix)
                    new_hypotheticals.append(("", new_cost, new_time))

            # try making edit (if allowed)
            if time > 0:
                continue
            new_cost = cost + 1
            for a in ascii_lowercase:
                if a == x:
                    # already considered above
                    continue
                new_prefix = prefix + a
                new_time = 5
                if trie.has_keys_with_prefix(new_prefix):
                    new_hypotheticals.append((new_prefix, new_cost, new_time))
                    if new_prefix in trie:
                        new_hypotheticals.append(("", new_cost, new_time))
        
        #print(new_hypotheticals)
        hypotheticals = new_hypotheticals
    # print(hypotheticals)
    return min(cost for (prefix, cost, time) in hypotheticals if prefix == "")

if __name__ == "__main__":
    import fileinput
    f = fileinput.input()
    T = int(f.readline())
    for case in range(1, T+1):
        email = f.readline().strip()
        answer = solve(email)
        print("Case #%d: %s" % (case, answer))
