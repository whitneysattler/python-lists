def isAnagram(s1, s2):
    lst1 = [x for x in s1]
    lst2 = [x for x in s2]
    lst1.sort()
    lst2.sort()
    if lst1 == lst2:
        return True
    return False

def main():
    inputString1 = input("Enter string 1: ")
    inputString2 = input("Enter string 2: ")
    if isAnagram(inputString1, inputString2):
        print("The words are an anagram")
        return
    print("The words are not an anagram")

main()
