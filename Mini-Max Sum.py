#!/bin/python3

import math
import os
import random
import re
import sys

# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
# Then print the respective minimum and maximum values as a single line of two space-separated long integers.
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    min1 = sum(arr)
    max1 = 0
    for x in range(5):
        min_temp = 0
        max_temp = 0
        for y in range(5):
            if y!=x:    
                max_temp=arr[y]+max_temp
                min_temp=arr[y]+min_temp
        if max_temp>=max1:
            max1 = max_temp
        if min_temp<=min1:
            min1 = min_temp
    print(f"{min1}  {max1}")

if __name__ == '__main__':

    #arr = list(map(int, input().rstrip().split()))
    arr = [1,2,3,4,5]
    miniMaxSum(arr)
