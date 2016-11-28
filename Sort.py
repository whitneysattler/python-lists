# The function for sorting elements in ascending order
def selectionSort(lst):
    for i in range(len(lst) - 1):
        currentMin = lst[i]
        minIndex = i

        for j in range(i + 1, len(lst)):
            if currentMin > lst[j]:
                currentMin = lst[j]
                minIndex = j

        #Swap the minimums
        if minIndex != i:
            lst[minIndex] = lst[i]
            lst[i] = currentMin

# The function for sorting elements in ascending order
def insertionSort(lst):
    for i in range(1,len(lst)):
        # insert lst[i] into a sorted sublist lst[0:i] so that
        # lst[0: i+1] is sorted.
        currentElement = lst[i]
        k = i - 1
        while k >= 0 and lst[k] > currentElement:
            lst[k + 1] = lst[k]
            k -= 1

        # Insert the current element into lst[k + 1]
        lst[k + 1] = currentElement
