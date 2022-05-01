from wordle_solver import findBestGuess

with open("allowed_words.txt", "r") as f:
    guessList = f.read().splitlines()

with open("possible_words.txt", "r") as f:
    answerList = f.read().splitlines()


class Solver:
    def __init__(self):
        pass

g, p = findBestGuess(answerList)
intro = 'The most optimal guess is: {gs}, which we expect to narrow the possible answers by {pt}'.format(gs = g, pt = p)

