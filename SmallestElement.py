def indexOfSmallestElement(lst):
    mini = lst[0]
    miniIndex = 0
    for i in range(1, len(lst)):
        if lst[i] < mini:
            mini = lst[i]
            miniIndex = i
    return miniIndex

def main():
    inputString = input("Enter a list of number (seperated by spaces): ")
    nums = [int(x) for x in inputString.split(" ")]
    print (indexOfSmallestElement(nums))

main()
