#!python3
"""Problem B. Full Binary Tree

https://code.google.com/codejam/contest/2984486/dashboard#s=p1A
A tree is a connected graph with no cycles.

A rooted tree is a tree in which one special vertex is called the root. If there is an edge between X and Y in a rooted tree, we say that Y is a child of X if X is closer to the root than Y (in other words, the shortest path from the root to X is shorter than the shortest path from the root to Y).

A full binary tree is a rooted tree where every node has either exactly 2 children or 0 children.

You are given a tree G with N nodes (numbered from 1 to N). You are allowed to delete some of the nodes. When a node is deleted, the edges connected to the deleted node are also deleted. Your task is to delete as few nodes as possible so that the remaining nodes form a full binary tree for some choice of the root from the remaining nodes."""
import networkx as nx

def largest_binary_tree(G, r, parent=None):
    """The MAXIMUM number of nodes in a subgraph of G that is a full binary tree with r its root."""
    neighbours = [x for x in G.neighbors(r) if x != parent]
    if len(neighbours) >= 2:
        possible_child_trees = [largest_binary_tree(G, x, parent=r) for x in neighbours]
        possible_child_trees.sort(reverse=True)
        return 1 + possible_child_trees[0] + possible_child_trees[1]

    return 1


def solve(G):
    """y is the minimum number of nodes to delete from G to make a full binary tree."""
    return len(G) - max(largest_binary_tree(G, x) for x in G)

if __name__ == "__main__":
    import fileinput
    f = fileinput.input()

    # The first line of the input gives the number of test cases, T. T test cases follow. The first line of each test case contains a single integer N, the number of nodes in the tree. The following N-1 lines each one will contain two space-separated integers: Xi Yi, indicating that G contains an undirected edge between Xi and Yi.
    T = int(f.readline())

    for case in range(1, T+1):
        N = int(f.readline())
        G = nx.Graph()
        G.add_nodes_from(range(1, N+1))
        for i in range(N-1):
            X, Y = [int(x) for x in f.readline().split()]
            G.add_edge(X, Y)

        assert(nx.is_connected(G))
        answer = solve(G)
        print("Case #{0}: {1}".format(case, answer))

