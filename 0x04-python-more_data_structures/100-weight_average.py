#!/usr/bin/python3
def weight_average(my_list=[]):
    sum_score = 0
    weighted_sum = 0
    if not my_list:
        return 0
    else:
        for i in my_list:
            total_score = i[0]*i[1]
            sum_score += total_score
            weighted_sum += i[1]
        average = (sum_score / weighted_sum)
        return average
