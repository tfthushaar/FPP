def convertToList(string):
    pairs = string.split(';')
    result = []
    for i in pairs:
        value = i.split('=')
        result.append(value)
    return result

inputString = "a=b;c=d;e=f;g=h"
outputList = convertToList(inputString)
print(outputList)