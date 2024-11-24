def quicksort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[0]
        less = [x for x in lst[1:] if x >= pivot]  # Membandingkan elemen yang lebih besar atau sama dengan pivot
        greater = [x for x in lst[1:] if x < pivot]  # Membandingkan elemen yang lebih kecil dari pivot
        return quicksort(less) + [pivot] + quicksort(greater)

lst = [88, 19, 28, 100, 87]
hasil = quicksort(lst)
print(hasil)
