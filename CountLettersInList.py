import RandomCharacter #

def main():
    # Create a list of characters
    chars = [RandomCharacter.getRandomLowerCaseLetter() for x in range(100)]

    # Display the list
    print("The lowercase letters are:")
    displayList(chars)

    # Count the occurences of each letter
    counts = countLetters(chars)

    # Display counts
    print()
    print("The occurences of each letter are:")
    displayCounts(counts)

# Display the list of characters
def displayList(chars):
    for i in range(len(chars)):
        if (i + 1) % 20 == 0:
            print (chars[i])
        else:
            print (chars[i], end = " ")

# Count the occurences of each letter
def countLetters(chars):
    counts = [0 for i in range(26)]
    for char in chars:
        counts[ord(char) - ord("a")] += 1
    return counts

# Display the counts
def displayCounts(array):
    for i in range(len(array)):
        if ((i + 1) % 13 == 0):
            print (chr(ord('a') + i) + ":" + str(array[i]))
        else:
            print (chr(ord('a') + i) + ":" + str(array[i]), end = " ")

main()
