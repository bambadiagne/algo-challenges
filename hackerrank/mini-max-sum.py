def miniMaxSum(arr):
    arr.sort()
    print(f'{sum(arr[:-1])} {sum(arr[1:])}')