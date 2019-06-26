from Algs.SortHelp import *

class ElementarySorts:
    def sort(arr, strategy):
        if(strategy == "selection"):
            ElementarySorts.execute_selection_sort(arr)
        elif(strategy == "insertion"):
            ElementarySorts.execute_insertion_sort(arr)
        elif(strategy == "shell"):
            ElementarySorts.execute_shell_sort(arr)

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

    def execute_shell_sort(arr):
        if precheck_arr(arr):
            return arr
        h=1
        while h<len(arr)//3:
            h = 3*h+1
        while h>=1:
            i = h
            while i < len(arr):

                j = i
                while j>=h:
                    if arr[j]<arr[j-h]:
                        exchange(arr, j, j-h)
                    j-=1
                i+=1
            h=h//3
        return arr