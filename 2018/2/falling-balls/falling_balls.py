from itertools import accumulate

T = int(input())
for case in range(1, T+1):
    C = int(input())
    B = [int(x) for x in input().split()]
    assert len(B) == C
    assert sum(B) == C
    
    progress = [1]*C
    rows = list()
    while progress != B:
        row = ""
        delta = [p-b for p,b in zip(progress,B)]
        accumulated = [0] + list(accumulate(delta))
        for i in range(C):
            a = accumulated[i]
            if a < 0:
                row += "/"
                progress[i] -= 1
                progress[i-1] += 1
            elif a > 0:
                row += "\\"
                progress[i] -= 1
                progress[i+1] += 1
            else:
                row += "."
        if "\/" in row or row[0] != "." or row[-1] != ".":
            rows = False
            break
        rows.append(row)
        
    if progress == B:
        rows.append("."*C)

    print("Case #{}: {}".format(case, len(rows) if rows else "IMPOSSIBLE"))
    if rows:
        for row in rows:
            print("".join(row))
