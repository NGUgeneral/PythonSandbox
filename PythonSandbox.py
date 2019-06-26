import time
import datetime
from Algs.ElementarySorts import *

#Testing SelectionSort

arr = list(range(0, 10))
arr += range(0, 10)
knuth_shuffle(arr)

start = datetime.datetime.now()
ElementarySorts.sort(arr, "shell")
benchmark = datetime.datetime.now() - start
print("IsSorted: " + str(is_sorted(arr)))
print("Time spent: " + str(benchmark))