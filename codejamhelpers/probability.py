def trials(P):
    """Given the individual probabilities P[i] of n independent trials, calculate the probabilities Q[k] that exactly :math:`0 \le k \le n` are successful."""
    Q = [1]
    for p in P:
        Q = [(1-p) * Q[0]] + [(1-p) * Q[i] + p*Q[i-1] for i in range(1,len(Q))] + [p*Q[-1]]

    return Q
