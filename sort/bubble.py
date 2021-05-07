def bubble_sort(seq, asc=True):    
    for outer in range(len(seq)):
        for inner in range(outer+1, len(seq)):
            if asc and seq[outer] > seq[inner]:
                swap(seq, outer, inner)
            elif not asc and seq[outer] < seq[inner]:
                swap(seq, outer, inner)

    return seq

def swap(seq, one, two):
    seq[one] = seq[one] + seq[two]
    seq[two] = seq[one] - seq[two]
    seq[one] = seq[one] - seq[two]
    return seq

print(bubble_sort([2,1,5,6,3,8,6,4,7,88,4,5,67,34,32,56,78,79,234,90,77,68,85]))
print(bubble_sort([2,1,5,6,3,8,6,4,7,88,4,5,67,34,32,56,78,79,234,90,77,68,85], False))