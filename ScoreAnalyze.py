def main():
    scoresString = input("Enter scores: ")
    scores = [float(x) for x in scoresString.split(" ")]
    average = sum(scores) / len(scores)
    below = 0
    above = 0
    for score in scores:
        if score >= average:
            above += 1
        else:
            below += 1
    print("The average is " + str(average))
    print("There are " + str(above) + " scores above or equal to the average")
    print("There are " + str(below) + " scores below the average")

main()
