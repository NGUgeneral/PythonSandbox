from Algs.SortHelp import *

class SelectionSort:
    def execute_selection_sort(arr):
        if arr == None:
            raise ValueError("Can't sort null")
        lim = len(arr)
        if lim<2:
            return arr
        i = 0
        while i<lim-1:
            j = i + 1
            while j < lim:
                if arr[j]<arr[i]:
                    exchange(arr, i, j)
                    break
                j+=1
            i+=1
        return arr