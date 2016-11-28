def main():
    numbersInput = input("Enter numbers: ")
    numbers = numbersInput.split(" ")
    for i in range(len(numbers)):
        print(numbers[len(numbers) - 1 - i], end = " ")
    print()
    
main()
