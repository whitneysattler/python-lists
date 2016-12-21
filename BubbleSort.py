def bubbleSort(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1):
            if (lst[j] > lst[j + 1]):
                lst[j], lst[j+1] = lst[j+1], lst[j]
                sorted = False
        if sorted:
            break
    return lst

def main():
    inputString = input("Enter numbers: ")
    nums = [int(x) for x in inputString.split(" ")]
    print (bubbleSort(nums))

main()
