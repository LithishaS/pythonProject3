string = input("Enter the word:")
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for i in range(len(string)):
    if string[i] not in vowels:
        print(string[i])
