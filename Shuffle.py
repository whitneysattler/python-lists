from random import randint

def shuffleIt(lst):
    for i in range(len(lst)):
       index = randint(i, len(lst) - 1)
       lst.insert(0, lst.pop(index))

def main():
    inputString = input("Enter numbers: ")
    nums = [int(x) for x in inputString.split(" ")]
    shuffleIt(nums)

    print (nums)

main()
