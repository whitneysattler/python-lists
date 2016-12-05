def mean(lst):
    return sum(lst)/len(lst)

def deviation(lst):
    average = mean(lst)
    diffSum = 0
    for i in range(len(lst)):
        diffSum += ((lst[i] - average) ** 2)
    return (diffSum / (len(lst) - 1)) ** (1/2)

def main():
    inputString = input("Enter numbers: ")
    nums = [float(x) for x in inputString.split(" ")]
    print ("The mean is " + str(mean(nums)))
    print ("The standard deviation is " + str(deviation(nums)))

main()
