def most_frequent(grid):
    all = "".join(grid)
    return max(all.count("W"), all.count("B"))

T = int(input())
for case in range(1, T+1):
    R, C = [int(x) for x in input().split()]
    grid = [input() for i in range(R)]
    assert all(len(row) == C for row in grid)

    best = 0
    for i in range(R):
        for j in range(C):
            topleft = [row[:j] for row in grid[:i]]
            topright = [row[j:] for row in grid[:i]]
            bottomleft = [row[:j] for row in grid[i:]]
            bottomright = [row[j:] for row in grid[i:]]
            size = sum(most_frequent(quad) for quad in (topleft, topright, bottomleft, bottomright))
            best = max(size, best)

    solution = best
    print("Case #{}: {}".format(case, solution))
