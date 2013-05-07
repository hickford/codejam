#!python
# https://code.google.com/codejam/contest/2434486/dashboard
# Armin is playing Osmos, a physics-based puzzle game developed by Hemisphere Games. In this game, he plays a "mote", moving around and absorbing smaller motes.

# Lemma: Given a feasible solution that deletes a mote size x and adds a larger mote size y, there is a superior feasible solution for which all the motes added are smaller than all those deleted (rather than delete the mote size x, eat it after the larger mote size y).

import fileinput
f = fileinput.input()

T = int(f.readline())

def solve(A, motes):
	motes = sorted(motes)
	N = len(motes)

	best_strategy = N	# delete all

	if A == 1:
		# can't eat any ever.
		return N

	additions = 0

	while motes:
		if motes[0] < A:
			# eat!
			A += motes.pop(0)
		else:
			# how about deleting all the remaining motes (by the lemma)
			deletion_strategy = additions + len(motes)
			best_strategy = min(best_strategy, deletion_strategy)

			# add (and eat) motes until edible
			while A <= motes[0]:
				A += A-1
				additions += 1

	return min(additions, best_strategy)


for case in range(1,T+1):
	A, N = [int(x) for x in f.readline().split()]
	motes = [int(x) for x in f.readline().split()]
	assert len(motes) == N

	answer = solve(A, motes)

	print "Case #%d: %d" % (case, answer)










