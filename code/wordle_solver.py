import numpy as np
import math
import random
from collections import Counter

with open("allowed_words.txt", "r") as f:
    guessList = f.read().splitlines()

with open("possible_words.txt", "r") as f:
    answerList = f.read().splitlines()

dict = {}

def getEV(guess, ans_list):
    ev = 0
    fr_tracker = {}
    for answer in ans_list:
        ret = ['b']*5
        for i in range(5):
            if guess[i] == answer[i]:
                ret[i] = 'g'
        for j in range(5):
            if ret[j] != 'g':
                for k in range(5):
                    if ret[k] == 'b':
                        if guess[j] == answer[k]:
                            ret[j] = 'y'
        ret = ''.join(map(str, ret))
        if ret in fr_tracker:
            fr_tracker[ret] += 1
        else:
            fr_tracker[ret] = 1
    for key, value in fr_tracker.items():
        x = value/len(ans_list)
        ev += x*(math.log(1/x,2))
    return ev

def findBestGuess(aL):
    for g in guessList:
        dict[g] = getEV(g, aL)
    c = Counter(dict)
    mostCommon = c.most_common(1)
    #word, value = mostCommon
    return mostCommon

print(findBestGuess(answerList))