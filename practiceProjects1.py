'''
Practice Projects
pg 102
'''

#Comma Code

#takes a list and returns a string separated with
#commas and a space and with and inserted before
#the last item

spams = ['apples','bannanas','tofu','cats']
spam = ['apples','bannanas','tofu','cats']

def commaCode(l):
    for i in range(0,len(l)):
        if(l[i] == l[len(l) - 1]):
            l[i] =  'and ' + l[i]
        else:
            l[i] = l[i] + ', '
    return ''.join(l)
print(commaCode(spams))

def stackCommaCode2(words):
    if len(words) == 1:
        return words[0]
    return '{}, and {}'.format(', '.join(words[:-1]),words[-1])
print(stackCommaCode2(spam))


#character picture grid#
'''
we want this
..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....

'''

grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]


def drawGrid(grid):
    str = ''
    for i in range(len(grid)):
        str +='\n'
        for j in range(len(grid)):
            if i > 5:
                break;
            str += grid[j][i]
    return str
print(drawGrid(grid))


'''
first row:
grid[0][0]
grid[1][0]
grid[2][0]
grid[3][0]
.....
grid[8][0]


then the program should print out
grid[0][1]
grid[1][1]
grid[2][1]

last will be:
grid[8,5]
'''
