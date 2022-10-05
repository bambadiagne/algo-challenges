def divisibleSumPairs(n, k, ar):
    pair_numbers = 0
    for i in range(n):
        for j in range(n):
            if ((ar[i]+ar[j]) % k == 0 and i < j):
                pair_numbers += 1

    return pair_numbers
