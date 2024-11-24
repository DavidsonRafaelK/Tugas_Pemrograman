def bubblesort (lst):
  for i in range (len(lst)):
    for j in range (0, len(lst) - i - 1):
      if (lst[j] < lst[j+1]):
        lst[j], lst[j+1] = lst[j+1], lst[j]
  return lst

lst = [88, 19, 28, 100, 87]
hasil = bubblesort(lst)
print(hasil)