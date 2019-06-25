from Tutorial.TutorialMaster import TutorialMaster
from Tutorial.Parent import Parent
from Algs.SelectionSort import *
from Algs.SortHelp import *

#Testing SelectionSort
arr = [0, 0, 1, 0, 3, 4]

print_arr(arr)
sorted_arr = SelectionSort.execute_selection_sort(arr)
print_arr(sorted_arr)
print("IsSorted: " + str(is_sorted(sorted_arr)))