def main():
    scores = input("Enter scores: ")
    scoreL = scores.split(" ")
    scoreLst = [int(x) for x in scoreL]
    best = max(scoreLst)

    for i in range(len(scoreLst)):
        dif = best - int(scoreLst[i])
        if dif == 0:
            dif = 1
        grade = chr(((dif - 1) // 10 + ord("A")))
        if grade not in ["A", "B", "C", "D"]:
            grade = "F"
        print ("Student " + str(i + 1) + " score is " + str(scoreLst[i]) + " and grade is " + grade)

main()
