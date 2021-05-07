def quick_sort(seq):
    if len(seq) <= 1:
        return seq
    else:
        pivot = seq.pop()
        greater = []
        smaller = []
        for val in seq:
            if val > pivot:
                greater.append(val)
            else:
                smaller.append(val)

        return quick_sort(smaller) + [pivot] + quick_sort(greater)

print(quick_sort([2,1,5,6,3,8,6,4,7,88,4,5,67,34,32,56,78,79,234,90,77,68,85]))