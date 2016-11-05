def linearSearch(lst, key):
    for i in range(len(lst)):
        if lst[i] == key:
            return i
        
    return -1

def binarySearch(lst, key):
    high = len(lst) - 1
    low = 0
    while high >= low:
        mid = (high + low) // 2
        print (str(low) + ", " + str(mid) + ", " + str(high))
        if lst[mid] == key:
            return mid
        if lst[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1
