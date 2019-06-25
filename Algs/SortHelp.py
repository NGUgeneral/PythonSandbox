def exchange(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def is_sorted(arr):
    if arr == None:
        return False
    if len(arr) < 2:
        return True
    i = 1
    while i < len(arr):
        if arr[i] < arr[i - 1]:
            return False
        i+=1
    return True

def print_arr(arr):
    print(", ".join(map(str, arr)))

def precheck_arr(arr):
    if arr == None:
        raise ValueError("Can't sort null")
    if len(arr)<2:
        return True
    return False