import time
import datetime
from Algs.ElementarySorts import *
from Algs.SortHelp import *

#Testing SelectionSort
#arr = [ 5, 4, 2, 1, 3 ]
#arr = [ 5, 4, 2, 1, 3, 5, 4, 2, 1, 3 ]
arr = [0, 0, 1, 0, 3, 4, 0, 0, 1, 0, 3, 4, 0, 0, 1, 0, 3, 4]

print_arr(arr)
start = datetime.datetime.now()
ElementarySorts.execute_selection_sort(arr)
benchmark = datetime.datetime.now() - start
print_arr(arr)
print("IsSorted: " + str(is_sorted(arr)))
print("Time spent: " + str(benchmark))
