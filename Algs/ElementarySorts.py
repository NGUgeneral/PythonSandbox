from Algs.SortHelp import *

class ElementarySorts:
    def execute_selection_sort(arr):
        if precheck_arr(arr):
            return arr
        i = 0
        while i<len(arr)-1:
            j = i + 1
            min = j
            while j < len(arr):
                if arr[j]<arr[min]:
                    min = j
                j+=1
            exchange(arr, i, min)
            i+=1
        return arr

    def execute_insertion_sort(arr):
        if precheck_arr(arr):
            return arr
        i = 0
        while i<len(arr):
            j = i
            while j>0:
                if arr[j]<arr[j-1]:
                    exchange(arr, j-1, j)
                    j-=1
                else:
                    break
            i+=1
        return arr