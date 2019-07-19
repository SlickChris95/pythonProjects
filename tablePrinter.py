'''
Write a function named printTable() that takes a list of
lists of strings and displays it in a well-organized table
with each column right-justified.Assume that all the inner
lists will contain the same number of strings.For example,
the value could look like this

'''

tableData = [['apples', 'oranges', 'cherries', 'bananas'],
['Alice', 'Bob', 'Carol', 'Davidsss'],
['dogs', 'cats', 'moose', 'goosess']]


def longestWord(some_list):
    count = 0    #You set the count to 0
    for i in some_list: # Go through the whole list
        if len(i) > count: #Checking for the longest word(string)
            count = len(i)
            word = i
    return ("the longest string is " + word)

print(longestWord(tableData[-1]))
