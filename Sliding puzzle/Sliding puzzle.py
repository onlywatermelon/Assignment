import random
import bisect
import copy

def pos_int():                                                #Determine the integer
    while True:
        try:
            K = int(input('Enter the postive integer:'))
            if K >= 3 and K <= 10:
                return K
            else:
                K = int('str')                                #Create the error.
            break
        except:
            print('Error! It should be the positive integer.', end='')

def print_numbers():                                          #Optimised number alignment for better aesthetics. No using the '\t'.
    for i in range((n**2)):
        if num_list[i] == 0:
            print('   ',end='')
        elif num_list[i] < 10:
            print(num_list[i],' ',end='')
        else:
            print(num_list[i],'',end='')
        if (i+1)%n == 0:
            print()

def solvable(l: list) -> int:                                 #Use the inversion to determine the solvabilty of the puzzle.
    tem_list, inversion = [], 0                               #True meas solvable.
    for i in reversed(range(0, n)):                           #Ref. Wm. W Johnson, & Story, W. (1879). Notes on the "15" Puzzle. American Journal of Mathematics, 2(4), 397-404. doi:10.2307/2369492
        pairs_of_invers = bisect.bisect_left(tem_list, l[i])  #Use bisection to optimise algorithms.
        inversion += pairs_of_invers
        tem_list.insert(pairs_of_invers, l[i])
    row_and_col = num_list.index(0)
    print('inever',inversion)
    if n%2 == 1 and inversion%2 == 0:
        return True
    elif n%2 == 0 and ((row_and_col//n)+inversion)%2 == 1:
        return True
    else:
        return False

def option_limit_and_hint():                                  #
    global move
    Up, Down, Left, Right= ["Up", 'w'], ["Down", 's'], ["Left", 'a'], ["Right", 'd']
    option = [Up,Down,Left,Right]
    row_and_col = num_list.index(0)
    if row_and_col >= n*(n-1):
        option.remove(Up)     
    if row_and_col < n:
        option.remove(Down)    
    if row_and_col % n == (n-1):
        option.remove(Left)    
    if row_and_col % n == 0:
        option.remove(Right)
    move_limit = [option[i][1] for i in range(len(option))]
    print("Next:", *option, sep = '')
    move = input()
    while move in move_limit:
        return True
    else:
        print('Error! Please press the given key.')
        print_numbers()

def play():
    row_and_col = num_list.index(0)
    print(row_and_col)
    print(num_list[row_and_col])
    if move == directions[0]:
        num_list[row_and_col], num_list[row_and_col+n] = num_list[row_and_col+n], num_list[row_and_col]
    elif move == directions[1]:
        num_list[row_and_col], num_list[row_and_col-n] = num_list[row_and_col-n], num_list[row_and_col]
    elif move == directions[2]:
        num_list[row_and_col], num_list[row_and_col+1] = num_list[row_and_col+1], num_list[row_and_col]
    elif move == directions[3]:
        num_list[row_and_col], num_list[row_and_col-1] = num_list[row_and_col-1], num_list[row_and_col]
    else:
        print("Error")

n = pos_int()
num_list = list(reversed([i for i in range(n**2)]))
num_list_0 = copy.deepcopy(num_list)
directions = ['w','s','a','d']
random.shuffle(num_list)

while not solvable(num_list):
    random.shuffle(num_list)

print_numbers()

while num_list != num_list_0:
    if option_limit_and_hint():
        play()
        print_numbers()
else:
    print('Win!')
