def multiply(arr):
    F = G = [1]*len(arr)
    for i in range(1, len(arr)):
        F[i] = arr[i-1]*F[i-1]
    for i in range(len(arr)-2, -1, -1):
        G[i] = arr[i+1]*G[i+1]

    return [x*y for x, y in zip(F, G)]