def exchange(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def is_sorted(arr):
    if arr == None:
        return False
    lim = len(arr)
    if lim < 2:
        return True
    i = 1
    while i < lim:
        if arr[i] < arr[i - 1]:
            return False
        i+=1
    return True

def print_arr(arr):
    print(", ".join(map(str, arr)))