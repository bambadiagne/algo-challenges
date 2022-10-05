def diagonalDifference(arr):
    diago = 0
    n = len(arr)
    for i in range(n):
        diago += arr[i][i]
    for i in range(n-1, -1, -1):
        if (n > 1):
            diago -= arr[n-1-i][i]
        else:
            diago -= arr[0][0]
    return abs(diago)
