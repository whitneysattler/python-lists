def main():
    numsString = input("Enter ten numbers: ")
    nums = numsString.split(" ")
    distinct = []
    for num in nums:
        if num not in distinct:
            distinct.append(num)
    print ("The distinct numbers are: " + " ".join(distinct))

main()
