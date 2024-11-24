from typing import List

def find_max(lst: List, idx:int)->int:
  max = idx
  i = idx + 1
  while i != len(lst):
      if lst[i] > lst[max]:
          max = i
      i = i + 1
  return max

def selectionSort(lst: List):
  i = 0
  while i !=len(lst):
    biggest = find_max(lst, i)
    lst[i], lst[biggest] = lst[biggest], lst[i]
    i = i + 1
  return lst

lst = [88, 19, 28, 100, 87]
hasil = selectionSort(lst)
print(hasil)