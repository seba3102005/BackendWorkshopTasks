

with open('Week_1/input.txt','r') as file:
    lines = file.read().strip()   # use strip to remove any excess characters from the beginning and the end of the string
    words = lines.split()
    print(len(words))

    with open('Week_1/output.txt','w') as outputFile:
        outputFile.write(f"Word Counter: {len(words)} words")



