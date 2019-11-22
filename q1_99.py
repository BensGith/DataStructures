### Exercise 3 - q1: Dynamic Programming ###

### Template ###

# import libraries:
import numpy as np


# a. main function

def knapsack_bottom_up(items, maximum_weight):
    mat = np.zeros((len(items), maximum_weight + 1), dtype=int)
    for i in range(len(items)):
        for j in range(maximum_weight + 1):
            if items[i][0] > j:
                mat[i, j] = mat[i - 1, j]  # item is too heavy
                continue
            mat[i, j] = max(mat[i - 1, j], mat[i - 1, j - items[i][0]] + items[i][1])
    total_value = mat.max()  # max value of algorithm is max value in thr matrix
    packed = []
    temp = total_value
    while temp > 0:  # loop for recreating solution
        i = np.argmax(mat == temp)  # find first occurrence of remaining value, recreating items taken by row number
        row_id = int(i // (maximum_weight + 1))  # the row of the item taken
        temp -= items[row_id][1]  # decrease value according to item taken and look for next item
        packed.append(items[row_id])  # add item to packed item list
    packed = sorted(packed, key=lambda x: x[0], reverse=True)  # sorts item list by weight from high to low
    print(total_value, packed)
    return total_value, packed


# b. subset-sum function (remember 3 code line is 3 points extra!)

def subset_sum_algo(numbers, subset_sum):
    lst = [(e, e) for e in numbers]  # converting list to list of tuples
    w, packed = knapsack_bottom_up(lst, subset_sum)  # storing the optimal solution in w
    return subset_sum == w  # if w is equal to the goal sum, then return True, else return False


