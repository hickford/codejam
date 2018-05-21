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
        required_to_left = 0
        seen_so_far = 0
        row = ""
        new_progress = [0]*C
        for i, p in enumerate(progress):
            seen_so_far += p
            if p == 0:
                row += "."
            elif required_to_left >= seen_so_far:
                row += "/"
                new_progress[i-1] += p
            elif required_to_left + B[i] >= seen_so_far:
                row += "."
                new_progress[i] += p
            else:
                row += "\\"
                new_progress[i+1] += p
                
            required_to_left += B[i]
        if "\\/" in row or not row.startswith(".") or not row.endswith("."):
            rows = False
            break
        rows.append(row)
        progress = new_progress
        
    if progress == B:
        rows.append("."*C)

    print("Case #{}: {}".format(case, len(rows) if rows else "IMPOSSIBLE"))
    if rows:
        for row in rows:
            print("".join(row))
