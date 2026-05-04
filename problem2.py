def min_operations(arr, k):
    rem = arr[0] % k

    for x in arr:
        if x % k != rem:
            return -1

    arr.sort()
    mid = arr[len(arr)//2]

    steps = 0
    for x in arr:
        steps += abs(x - mid) // k

    return steps


arr = [2, 4, 6, 8, 10]
k = 2

print(min_operations(arr, k))
