from typing import List

def insertion(lst: List, idx: int):
  i = idx
  print(f"iterasi ke {i}")
  while i > 0 and lst[i-1] < lst[idx]:
    i = i - 1
  value = lst[idx]
  print(f"{value}")
  del lst[idx]
  lst.insert(i, value)
  print(lst)

def insertionSort(lst: List):
  i = 0
  while i != len(lst): # ini kan untuk iterasi dari awal list sampai akhir
    insertion(lst, i) # 
    i = i - 1
  return lst

lst = [88, 19, 28, 100, 87] # [ 19, 28, 100, 87, 88]
hasil = insertionSort(lst)
print(hasil)