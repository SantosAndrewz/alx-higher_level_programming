#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    wgt_score_sum = 0
    wgt_sum = 0
    for score, weight in my_list:
        wgt_score_sum += score * weight
        wgt_sum += weight
    if wgt_sum == 0:
        return 0
    else:
        return (wgt_score_sum / wgt_sum)      
