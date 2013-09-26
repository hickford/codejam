#!python
import string

vowels = "aeiou"
consonants = "".join(x for x in string.ascii_lowercase if x not in vowels)

def solve(name, n):
    assert 0 < n <= len(name)
    value = 0

    run = 0 # run of consecutive consonants
    last_group_start_pos = None

    for (i, letter) in enumerate(name):
        if letter in consonants:
            run += 1
            if run >= n:
                last_group_start_pos = i - n + 1
        else:
            run = 0
              
        if last_group_start_pos == None:
            continue

        # substrings = [name[j:i+1] for j in range(last_group_start_pos+1)]
        # print substrings
        
        value += last_group_start_pos + 1

    return value

if __name__ == "__main__":
    import fileinput
    f = fileinput.input()
    T = int(f.readline())
    for i in range(1,T+1):
        name, n = f.readline().split()
        n = int(n)

        value = solve(name, n)
        print "Case #%d: %s" % (i, value)
