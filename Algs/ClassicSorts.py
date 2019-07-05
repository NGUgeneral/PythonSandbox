def execute_merge_sort(arr):
    aux = [0] * len(arr)
    return sort_iteration(arr, aux, 0, len(arr) - 1)


def sort_iteration(arr, aux, lo, hi):
    if lo >= hi:
        return
    mid = lo+(hi-lo)//2
    sort_iteration(arr, aux, lo, mid)
    sort_iteration(arr, aux, mid+1, hi)
    merge(arr, aux, lo, mid, hi)


def merge(arr, aux, lo, mid, hi):
    k = lo
    while k <= hi:
        aux[k] = arr[k]
        k += 1
    i = lo
    j = mid+1
    k = lo
    while k <= hi:
        if i > mid:
            arr[k] = aux[j]
            j += 1
        elif j > hi:
            arr[k] = aux[i]
            i += 1
        elif aux[i] < aux[j]:
            arr[k] = aux[i]
            i += 1
        else:
            arr[k] = aux[j]
            j += 1
        k += 1
    return arr
