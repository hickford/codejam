#!python3
from collections import defaultdict, OrderedDict

def cost(d, N):
    """The cost of travelling distance d on a line with N stations"""
    assert 0 <= d <= N-1
    return d*N - d*(d-1)//2
    
N = 10
assert cost(0, N) == 0
assert cost(1, N) == N
assert cost(2, N) == 2*N-1
assert cost(3, N) == 3*N-3
assert cost(N-1, N) == (N**2 + N - 2)//2

def naive_cost(journeys, N):
	expense = 0
	for (start, end, frequency) in journeys:
		expense += frequency * cost(end - start, N) 
	return expense

def solve(journeys, N):
	naive_expense = naive_cost(journeys, N)

	change_by_station = defaultdict(int)
	for (start, end, frequency) in journeys:
		change_by_station[start] += frequency
		change_by_station[end] -= frequency

	change_by_station = OrderedDict(sorted(change_by_station.items()))
	assert sum(change_by_station.values()) == 0

	clever_cost = 0

	train = OrderedDict()
	for (station, change) in change_by_station.items():
		if change == 0:
			continue
		if change > 0:
			train[station] = change
		else:
			people_to_leave = -change
			while people_to_leave > 0:
				last_station, last_lot = train.popitem()

				last_lot_to_leave = min(last_lot, people_to_leave)
				people_to_leave -= last_lot_to_leave
				clever_cost += last_lot_to_leave * cost(station - last_station, N)
				
				last_lot_to_remain = last_lot - last_lot_to_leave
				if last_lot_to_remain > 0:
					train[last_station] = last_lot_to_remain
	
	return naive_expense - clever_cost

if __name__ == "__main__":
	import fileinput
	f = fileinput.input()
	T = int(f.readline())
	for case in range(1,T+1):
		N, M = [int(x) for x in f.readline().split()]

		journeys = list()
		for i in range(M):
			start, end, frequency = [int(x) for x in f.readline().split()]
			journeys.append((start,end,frequency))

		answer = solve(journeys, N)
		print("Case #%d: %s" % (case, answer))