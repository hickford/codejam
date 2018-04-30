from sys import exit
T = int(input())
for case in range(1, T+1):
    A, B = (int(x) for x in input().split())
    N = int(input())
    for i in range(N):
        guess = (A+B+1)//2
        print(guess)
        result = input()
        if result == "CORRECT":
            break
        elif result == "TOO_BIG":
            B = guess - 1
        elif result == "TOO_SMALL":
            A = guess
        elif result == "WRONG_ANSWER":
            exit()
    else:
        exit()



