import numpy as np
import math
import random
import pickle


# with open("answerList", "rb") as fp:   # Unpickling
#     aL = pickle.load(fp)

with open("allowed_words.txt", "r") as f:
    guessList = f.read().splitlines()

with open("possible_words.txt", "r") as f:
    answerList = f.read().splitlines()

