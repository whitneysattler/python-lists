def main():
    primes = []
    i = 2
    while (len(primes) < 50):
        prime = True
        for num in primes:
            if (num > (i **(1/2))):
                break
            if (i % num == 0):
                prime = False
                break
        if prime:
            primes.append(i)
        i += 1

    print (str(primes))

main()
