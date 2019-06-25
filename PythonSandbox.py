from Tutorial.TutorialMaster import TutorialMaster
from Tutorial.Parent import Parent
import Algs.SortHelp


arr1 = None
arr2 = []
arr3 = [-1]
arr4 = [0, 0, 1, 2, 3, 4]
arr5 = [0, 0, 1, 0, 3, 4]

print("False: " + str(Algs.SortHelp.is_sorted(arr1)))
print("True: " + str(Algs.SortHelp.is_sorted(arr2)))
print("True: " + str(Algs.SortHelp.is_sorted(arr3)))
print("True: " + str(Algs.SortHelp.is_sorted(arr4)))
print("False: " + str(Algs.SortHelp.is_sorted(arr5)))
Algs.SortHelp.exchange(arr5, 2, 3)
print("True: " + str(Algs.SortHelp.is_sorted(arr5)))