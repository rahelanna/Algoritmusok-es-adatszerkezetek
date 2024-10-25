#!/bin/python3


import os


#
# Complete the 'powerSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER X
#  2. INTEGER N
#

def powerSum(X, N):
    # Write your code here
    # Belső rekurzív függvény
    def recursive_sum(X, N, num):
        # Az aktuális szám hatványának kiszámítása
        power = num ** N

        # Ha a hatvány nagyobb mint X visszatér 0-val
        if power > X:
            return 0

        # Ha a hatvány egyenlő X-szel, talált egy megoldást
        elif power == X:
            return 1

        # Az ajtuális szám használata, vagy kihagyása (két ág)
        else:
            return (recursive_sum(X - power, N, num + 1) +
                    recursive_sum(X, N, num + 1))

    # Rekurzió indítása az 1-es számmal
    return recursive_sum(X, N, 1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input().strip())

    N = int(input().strip())

    result = powerSum(X, N)

    fptr.write(str(result) + '\n')

    fptr.close()
