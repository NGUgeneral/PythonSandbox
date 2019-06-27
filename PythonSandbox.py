import time
import datetime
from Algs.ElementarySorts import *
from Algs.ClassicSorts import *

#Testing SelectionSort

arr = list(range(0, 100000))
arr += range(0, 100000)
knuth_shuffle(arr)

#print_arr(arr)
start = datetime.datetime.now()
ClassicSorts.sort(arr, "merge") #2000 with duplicates: 0.02s; 20000 with duplicates: 0.35s; 200000 with duplicates: 4.1s
#ElementarySorts.sort(arr, "shell") #2000 with duplicates: 3.7s
#ElementarySorts.sort(arr, "insertion") #2000 with duplicates: 1.7s
#ElementarySorts.sort(arr, "selection") #2000 with duplicates: 0.7s
benchmark = datetime.datetime.now() - start
#print_arr(arr)
print("IsSorted: " + str(is_sorted(arr)))
print("Time spent: " + str(benchmark))