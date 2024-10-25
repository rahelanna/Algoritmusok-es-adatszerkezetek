#!/bin/python3


import os


#
# Complete the 'minimumLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#

def minimumLoss(price):
    # Write your code here
    # Az árak és indexük tárolása könyvtárban
    price_dict = {p: i for i, p in enumerate(price)}

    # Árak rendezése csökkenő sorrendben
    sorted_prices = sorted(price, reverse=True)

    # Minimális veszteség kezdeti értéke
    min_loss = float('inf')

    # Rendezett árak iterélálása
    for i in range(1, len(sorted_prices)):
        # Két egymást követő ár közötti veszteség kiszámítása
        loss = sorted_prices[i - 1] - sorted_prices[i]

        # Annak ellenőrzése, hogy a magasabb ár az alacsonyabb ár előtt szerepel-e az eredeti könyvtárban (price_dict)
        if price_dict[sorted_prices[i - 1]] < price_dict[sorted_prices[i]]:
            # min_loss frissítése, ha a veszteség kisebb, mint az eddigi
            min_loss = min(min_loss, loss)

    return min_loss


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
