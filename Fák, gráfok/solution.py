#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


#
# Complete the 'journeyToMoon' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY astronaut
#

def journeyToMoon(n, astronaut):
    # Write your code here
    graph = [[] for _ in range(n)]
    for a, b in astronaut:
        graph[a].append(b)
        graph[b].append(a)

    # Iteratív mélységi keresés
    def iterative_dfs(start, visited):
        stack = [start]
        size = 0
        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = True
                size += 1
                stack.extend(neighbor for neighbor in graph[node] if not visited[neighbor])
        return size

    # Az összes összefüggő komponens megkeresése
    visited = [False] * n
    components = []
    total_sum = 0
    squared_sum = 0

    for i in range(n):
        if not visited[i]:
            size = iterative_dfs(i, visited)
            total_sum += size
            squared_sum += size * size

    # Párok kiszámolása a különböző országokból
    total_pairs = (total_sum * (total_sum - 1) // 2) - (squared_sum - total_sum) // 2

    return total_pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    p = int(first_multiple_input[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()