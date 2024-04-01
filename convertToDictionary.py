def convertToDictionary(string):
    pairs = string.split(';')
    result = {}
    for pair in pairs:
        key, value = pair.split('=')
        result[key] = value
    return result

inputString = "a=b;c=d;e=f;g=h"
outputDict = convertToDictionary(inputString)
print(outputDict)
