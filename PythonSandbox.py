import datetime
from Algs.ISort import *

arr = list(range(0, 10))
arr += range(0, 10)
knuth_shuffle(arr)

print_arr(arr)
start = datetime.datetime.now()
sort(arr, "merge") #2000 with duplicates: 0.02s; 20000 with duplicates: 0.35s; 200000 with duplicates: 4.1s
sort(arr, "shell") #2000 with duplicates: 3.7s
sort(arr, "insertion") #2000 with duplicates: 1.7s
sort(arr, "selection") #2000 with duplicates: 0.7s
benchmark = datetime.datetime.now() - start
print_arr(arr)
print("IsSorted: " + str(is_sorted(arr)))
print("Time spent: " + str(benchmark))
