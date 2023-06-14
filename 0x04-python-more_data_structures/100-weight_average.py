#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_weight = sum(weight * value for weight, value in my_list)
    total_value = sum(value for _, value in my_list)

    return total_weight / total_value
