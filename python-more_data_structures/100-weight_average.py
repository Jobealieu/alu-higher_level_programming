#!/usr/bin/python3
def weight_average(my_list=None):
    if not my_list:
        return 0

    total_weighted_score = sum(score * weight for score, weight in my_list)
    total_weight = sum(weight for score, weight in my_list)

    return total_weighted_score / total_weight
