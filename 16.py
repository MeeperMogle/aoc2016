import re
sampleInput = '10000'
lengthSample = 20

input1 = '11101000110010100'
length1 = 272

input2 = '11101000110010100'
length2 = 35651584

def generateNext(a, requiredSize):
    b = ''

    # Reverse all characters replace 1 with 0 and vice-versa
    for character in a[::-1]:
        b += '0' if character == '1' else '1'

    # Put together a and b with a 0 in-between
    next = a + '0' + b

    # If it's big enough, return it (truncate overflowing data), if not use it as input for another iteration
    return next[0 : requiredSize] if len(next) >= requiredSize else generateNext(next, requiredSize)

def checksum(data):
    # Checksum starts as empty
    check = ''

    # Get all pairs of characters in the input data
    doubles = re.findall('.{1,2}', data);

    # For each pair, if they are the same add a 1, else add a 0, to checksum
    for twoChars in doubles:
        check += '1' if twoChars[0] == twoChars[1] else '0'

    # Once the checksum-length is odd (uneven pairs), that's final
    return check if len(check) % 2 == 1 else checksum(check)

sampleData = generateNext(sampleInput, lengthSample)
print('sample data:', sampleData)
print('sample checksum:', checksum(sampleData))

oneData = generateNext(input1, length1)
print('16.1 data:', oneData)
print('16.1 checksum:', checksum(oneData))

twoData = generateNext(input2, length2)
print('16.2 data:', '<omitted>')
print('16.2 checksum:', checksum(twoData))
