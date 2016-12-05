def main():
    numberString = input("Enter integers between 1 and 100: ")
    counts = [0 for i in range(1, 101)]
    numsLst = numberString.split(" ")
    nums = [int(x) for x in numsLst]

    for num in nums:
        counts[num - 1] += 1

    for i in range(len(counts)):
        if counts[i] != 0:
            print (str(i + 1) + " occurs " + str(counts[i]) + " times")

main()
