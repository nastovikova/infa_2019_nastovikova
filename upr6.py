
def set_difference(list1, list2):
    # Print difference between list1 and list2.
    result = []
    for elem1 in list1:
        fl = 1
        for elem2 in list2:
            if elem1 == elem2:
                fl = 0
        if fl == 1:
            result.append(elem1)
    print(result)


lst1 = [1, 3, 5, 7, 8]
lst2 = [2, 3, 4, 6, 8]
set_difference(lst1, lst2)
