# https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard
"""Saving The Universe Again
An alien robot is threatening the universe, using a beam that will destroy all algorithms knowledge. We have to stop it!

Fortunately, we understand how the robot works. It starts off with a beam with a strength of 1, and it will run a program that is a series of instructions, which will be executed one at a time, in left to right order. Each instruction is of one of the following two types:

C (for "charge"): Double the beam's strength.
S (for "shoot"): Shoot the beam, doing damage equal to the beam's current strength.
For example, if the robot's program is SCCSSC, the robot will do the following when the program runs:

Shoot the beam, doing 1 damage.
Charge the beam, doubling the beam's strength to 2.
Charge the beam, doubling the beam's strength to 4.
Shoot the beam, doing 4 damage.
Shoot the beam, doing 4 damage.
Charge the beam, increasing the beam's strength to 8.
In that case, the program would do a total of 9 damage.

The universe's top algorithmists have developed a shield that can withstand a maximum total of D damage. But the robot's current program might do more damage than that when it runs.

The President of the Universe has volunteered to fly into space to hack the robot's program before the robot runs it. The only way the President can hack (without the robot noticing) is by swapping two adjacent instructions. For example, the President could hack the above program once by swapping the third and fourth instructions to make it SCSCSC. This would reduce the total damage to 7. Then, for example, the president could hack the program again to make it SCSSCC, reducing the damage to 5, and so on.

To prevent the robot from getting too suspicious, the President does not want to hack too many times. What is this smallest possible number of hacks which will ensure that the program does no more than D total damage, if it is possible to do so?"""

T = int(input())
for case in range(1, T+1):
    D, P = input().split()
    D = int(D)
    damages = list()
    charge = 1
    for x in P:
        if x == "C":
            charge *= 2
        elif x == "S":
            damages.append(charge)

    hacks = 0
    while sum(damages) > D and max(damages) > 1:
        d = damages[-1]
        damages[-1] = d//2
        damages.sort()
        hacks += 1

    solution = hacks if sum(damages) <= D else "IMPOSSIBLE"
    print("Case #{}: {}".format(case, solution))
