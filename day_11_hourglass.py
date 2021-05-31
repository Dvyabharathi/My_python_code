import math
import os
import random
import re
import sys

R = 6
C = 6
arr = []
for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

def hourglass(arr):
    max_sum = 0
    
    if(R < 3 or C < 3):
        return -1
    for i in range(0, R-2):
        for j in range(0, C-2):
            SUM = (arr[i][j] + arr[i][j+1] + arr[i][j+2] +
                   arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
            if(SUM > max_sum):
                max_sum = SUM
            else:
                continue
    return max_sum

print(hourglass(arr))
