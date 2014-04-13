#!python3
"""Google Code Jam Qualification Problem A. Magic Trick
https://code.google.com/codejam/contest/2974486/dashboard#s=p0
Recently you went to a magic show. You were very impressed by one of the tricks, so you decided to try to figure out the secret behind it!

The magician starts by arranging 16 cards in a square grid: 4 rows of cards, with 4 cards in each row. Each card has a different number from 1 to 16 written on the side that is showing. Next, the magician asks a volunteer to choose a card, and to tell him which row that card is in.

Finally, the magician arranges the 16 cards in a square grid again, possibly in a different order. Once again, he asks the volunteer which row her card is in. With only the answers to these two questions, the magician then correctly determines which card the volunteer chose. Amazing, right?

You decide to write a program to help you understand the magician's technique. The program will be given the two arrangements of the cards, and the volunteer's answers to the two questions: the row number of the selected card in the first arrangement, and the row number of the selected card in the second arrangement. The rows are numbered 1 to 4 from top to bottom.

Your program should determine which card the volunteer chose; or if there is more than one card the volunteer might have chosen (the magician did a bad job); or if there's no card consistent with the volunteer's answers (the volunteer cheated)."""

if __name__ == "__main__":
    """The first line of the input gives the number of test cases, T. T test cases follow. Each test case starts with a line containing an integer: the answer to the first question. The next 4 lines represent the first arrangement of the cards: each contains 4 integers, separated by a single space. The next line contains the answer to the second question, and the following four lines contain the second arrangement in the same format."""

    import fileinput
    f = fileinput.input()

    T = int(f.readline())
    for case in range(1,T+1):
        first = list()
        first_answer = int(f.readline())
        for i in range(4):
            first.append([int(x) for x in f.readline().split()])
        first_relevant = first[first_answer-1]
        second = list()
        second_answer = int(f.readline())
        for i in range(4):
            second.append([int(x) for x in f.readline().split()])
        second_relevant = second[second_answer-1]    

        possibles = [x for x in first_relevant if x in second_relevant]
        if len(possibles) > 1:
            answer = "Bad magician!"
        elif len(possibles) == 1:
            answer = possibles[0]
        else:
            answer = "Volunteer cheated!"

        print("Case #{0}: {1}".format(case, answer))
