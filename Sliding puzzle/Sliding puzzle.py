import bisect
import random

def pos_int():
    #Enter an integer(order of the puzzle) in [3,7].
    while True:
        try:
            K = int(input('Enter the dimension of the number puzzle，which is an integer in [3,10]:'))
            if K >= 3 and K <= 10:
                return K
            else:
                K = int('str') #Create the error.
            break
        except:
            print('Error! It should be the integer in [3,10].')

def init():
    global n
    global num_list
    global count
    n = pos_int()
    num_list = [i for i in range(n**2)]
    random.shuffle(num_list)
    while not solvable(num_list):
        random.shuffle(num_list)
    count = 0

def print_numbers():
    #Displaying one-dimensional lists as puzzles.
    #Optimised number alignment for better aesthetics. Without using '\t'.
    for i in range((n**2)):
        if num_list[i] == 0:
            print('   ',end='')
        elif num_list[i] < 10:
            print(num_list[i],' ',end='')
        else:
            print(num_list[i],'',end='')
        if (i+1)%n == 0:
            print() 

def solvable(l):
    #Use the inversion to determine the solvabilty of the puzzle.
    #Ref. Wm. W Johnson, & Story, W. (1879). Notes on the "15" Puzzle. American Journal of Mathematics, 2(4), 397-404. doi:10.2307/2369492
    tem_list, inversion = [], 0
    for i in reversed(range(0, n**2)):
        pairs_of_invers = bisect.bisect_left(tem_list, l[i])  #Use bisection to optimise algorithms.
        inversion += pairs_of_invers
        tem_list.insert(pairs_of_invers, l[i])
    inversion -= num_list.index(0)
    row_and_col = num_list.index(0)
    if n%2 == 1 and inversion%2 == 0:
        return True  #True means solvable.
    elif n%2 == 0 and ((row_and_col//n)+inversion)%2 == 1:
        return True
    else:
        return False

def option_limit_and_hint():
    global direction
    Up, Down, Left, Right= ["Up", directions[0]], ["Down", directions[1]], ["Left", directions[2]], ["Right", directions[3]]
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
    dir_limit = [option[i][1] for i in range(len(option))]
    print("Next:", *option, sep = '')
    direction = input()
    while direction in dir_limit:
        return True
    else:
        print('Error! Please press the given key.')
        print_numbers()

def play():
    row_and_col = num_list.index(0)
    if direction == directions[0]:
        num_list[row_and_col], num_list[row_and_col+n] = num_list[row_and_col+n], num_list[row_and_col]
    elif direction == directions[1]:
        num_list[row_and_col], num_list[row_and_col-n] = num_list[row_and_col-n], num_list[row_and_col]
    elif direction == directions[2]:
        num_list[row_and_col], num_list[row_and_col+1] = num_list[row_and_col+1], num_list[row_and_col]
    elif direction == directions[3]:
        num_list[row_and_col], num_list[row_and_col-1] = num_list[row_and_col-1], num_list[row_and_col]

print('''Welcome to Sliding Puzzle!
You need to move the numbers so that they are in numerical order, from smallest to largest.
Good luck.''')

init()
while True:
    directions = input('Enter four different letters moving right, down, left and right, separated by commas(,).').split(',')
    temp = list(set(directions))
    if len(directions) == 4 and len(temp) == 4:
        break
    else:
        print('Error!')

print_numbers()
num_list_0 = [i for i in range(1,n**2)] +[0]

while num_list != num_list_0:
    if option_limit_and_hint():
        count += 1
        play()
        print_numbers()
        if num_list == num_list_0:
            print("Congratulations! You have done",count,"times to succeed!")
            con = input('''Do you want to have another round?\nPress 'y' to continue, press other keys to exit.''')
            if con == 'y':
                init()
                print_numbers()
            else:
                break
