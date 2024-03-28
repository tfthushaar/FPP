def convertToString(inputList):
    result = []
    for sublist in inputList:
        string = f'{sublist[0]}={sublist[1]}'
        result.append(string)
    return ';'.join(result)

inputTuple = [['a', 'b'], ['c', 'd'], ['e', 'f'], ['g', 'h']]
outputString = convertToString(inputTuple)
print(outputString)
