filePath = input("Input filename (sample.txt): ")
try:
    readingFile = open(filePath, "r")
    lineNo = 0
    print("Reading file contents: ")
    for line in readingFile:
        lineNo += 1
        print("Line " + str(lineNo) + ": " + line, end='')
    readingFile.close()
except FileNotFoundError:
    print("The file \"" + filePath + "\" does not exist")
