pattern = ["R", "B", "G", "R"]
print(pattern)

Guess = ["G", "B", "R", "B"]
pattern_copy = [x for x in pattern]


def check(Guess, temppattern):
    score = [0, 0]  # black pegs, white pegs
    j = 0
    for i in Guess:  # check for black pegs
        print(i, j)
        if temppattern[j] == Guess[j]:
            score[0] += 1

            temppattern[j] = "X"
            Guess[j] = "X"

        j += 1

    j = 0
    for i in Guess:  # check for white pegs
        if Guess[j] in temppattern and Guess[j] != "X":
            score[1] += 1

            temppattern[j] = "X"
            Guess[j] = "X"

    print(pattern, temppattern, Guess)
    return (score)


print(check(Guess, pattern))


def clue2(guess, code):
    guess_copy = [g for g in guess]
    code_copy = [c for c in code]

    score = [0, 0]  # blacks, whites

    for i, peg in enumerate(guess_copy):  # black pegs
        if peg == code_copy[i]:
            code_copy[i] = "x"
            guess_copy[i] = "x"
            score[0] += 1

    for i, peg in enumerate(guess_copy):  # white pegs
        if peg in code_copy and not peg == "x":
            code_copy[code_copy.index(guess_copy[i])] = "x"
            guess_copy[i] = "x"
            score[1] += 1

    return score
