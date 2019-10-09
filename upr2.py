
def sort_by_select(arr):
    # Enter a list of numbers, get it sorted.
    print(arr)
    for k in range(len(arr)):
        maxx = arr[k]
        ind = k
        for i in range(k+1, len(arr)):
            if arr[i] > maxx:
                maxx = arr[i]
                ind = i
        arr[ind], arr[k] = arr[k], arr[ind]


numbers = [8, 6, 1, 10, 15, 2, 4, 7]
sort_by_select(numbers)
print(numbers)
