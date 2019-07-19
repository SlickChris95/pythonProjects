import re
'''
Want to check if the string matches a number with pattern:
(123)914-1493 or 294-290-5204

'''
numRegex = re.compile(r'(\(\d\d\d\)|\d\d\d-)\d\d\d-\d\d\d\d')
mo = numRegex.search('heres my number son (123)914-1493')
print(mo.group())
mo = numRegex.search('heres my number son 123-914-1493')
print(mo.group())

consonantRegex = re.compile(r'[^aeiouAEIOU]')
consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')


beginsWithHello = re.compile(r'^Hello')
beginsWithHello.search('Hello world!')

#re.VERBOSE ignores white space and comments
phoneRegex = re.compile(r'''(
    (\d{3}|\(d{3}\))?               #area code
    (\s|-|\.)?                      #seperator
    \d{3}                           #first 3 digits
    (\s|-|\.)?                      #seperator
    \d{4}                           #last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?    # extension

)''',re.VERBOSE)
