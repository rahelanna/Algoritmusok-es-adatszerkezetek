from collections import Counter

MOD = 10 ** 9 + 7


# Faktoriálisok és inverzek tárolása
def compute_factorials(n, mod):
    factorials = [1] * (n + 1)
    invers = [1] * (n + 1)

    # Faktoriálisok számítása
    for i in range(2, n + 1):
        factorials[i] = factorials[i - 1] * i % mod

    # Az utolsó faktoriális inverzének számítása
    invers[n] = pow(factorials[n], mod - 2, mod)

    # i faktoriális inverzének számítása
    for i in range(n - 1, 0, -1):
        invers[i] = invers[i + 1] * (i + 1) % mod

    return factorials, invers


def count_permutations(s):
    characters = Counter(s)
    n = len(s)

    # Faktoriálisok és inverzek kiszámítása
    factorials, invers = compute_factorials(n, MOD)

    # Az összes permutáció számítása
    result = factorials[n]

    # Osztás a duplikált karakterek faktoriálisaival
    for db in characters.values():
        result = result * invers[db] % MOD

    return result


s = input().strip()
print(count_permutations(s))
