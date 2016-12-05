from random import randint

def main():
    counts = [0 for x in range(10)]
    while sum(counts) < 1000:
        counts[randint(0,9)] += 1

    print (str(counts))

main()
