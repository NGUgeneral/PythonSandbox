import time
import datetime
from Algs.ElementarySorts import *
from Algs.SortHelp import *

#Testing SelectionSort
arr = [0, 0, 1, 0, 3, 4]


print_arr(arr)
start = datetime.datetime.now()
sorted_arr = ElementarySorts.execute_selection_sort(arr)
benchmark = datetime.datetime.now() - start
print_arr(sorted_arr)
print("IsSorted: " + str(is_sorted(sorted_arr)))
print("Time spent: " + str(benchmark))
