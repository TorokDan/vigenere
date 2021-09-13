#!venv/bin/python3

testString = 'almakorte'

testChar = testString.find('k')

# teststring = testString[4:] + testString[:4]

print(testString[testChar:] + testString[:testChar])