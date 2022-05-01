import math

#VARIABLE DECLARATIONS
max_info = 0
cs_list = []            #length = 343 ex: SXXGS
guess_list = ["porch", "heist", "zesty", "aabbe", "cleep"]         #len 13,000
answer_list = ["porch", "heist", "zesty"]        #originally len 2315
info_dict = {}
count = 0

#FIND NEXT GUESS
for g in guess_list:
    info_sum = 0
    for c in cs_list:
        count = 0
        for a in answer_list:
            #if answer g fits into color scheme c given correct answer a
                count += 1
        prob_c = count/len(answer_list)
        info = prob_c * math.log((1/prob_c), 2)
        info_sum += info
    expected_info = info_sum/343                #is div by 343 right?
    info_dict[g] = expected_info
    if expected_info > max_info:
        max_info = expected_info
        
guess = info_dict.index(max_info)




