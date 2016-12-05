def reverseList(lst):
    for i in range(1, len(lst)):
        lst.insert(0, lst.pop(i))

def main():
    inputString = input("Enter numbers: ")
    nums = [int(x) for x in inputString.split(" ")]
    reverseList(nums)

    print (nums)

main()
