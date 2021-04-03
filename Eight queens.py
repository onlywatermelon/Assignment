'''
The eight queens problem can be equivalent to such a problem,
i.e. Looking for a sort of 8 digits from 0 to 7(as queenList), s.t. abs(queenList[i]-queenList[j]) != abs(i-j)
for all i, j in [0,7] and i != j.
Problems about sorting use recursion to find all the answers
Ref. Chen, Z., Li, Q. and Wang, C., 2018. Design and Analysis of Algorithm Using Python. Tsinghua University Press.
'''
import random

def valid(colunm, tem):
    row = len(tem)
    for i in range(row):
        if abs(colunm - tem[i])/(row - i) == 1 or colunm in tem:
            return False
    return True

def queen(tem=[]):
    for colunm in range(8):
        if valid(colunm, tem):
            if len(tem) == 7:
                yield [colunm]
            else:
                for result in queen(tem + [colunm]):
                    yield result + [colunm]

def display(queenList:list):
    for i in queenList:
        print('| '*i,'|Q','| '*(7-i),'|',sep='')

r = random.randint(0,92)
display(list(queen())[r])
