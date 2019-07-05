from Algs.ElementarySorts import *
from Algs.ClassicSorts import *


def sort(arr, strategy):
    if precheck_arr(arr):
        return arr
    if strategy == "selection":
        execute_selection_sort(arr)
    elif strategy == "insertion":
        execute_insertion_sort(arr)
    elif strategy == "shell":
        execute_shell_sort(arr)
    elif strategy == "merge":
        execute_merge_sort(arr)
