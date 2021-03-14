import math

def pos_int(): 
    while True:
        try:
            K = int(input('Enter the integer:'))
            if K > 1:
                return K
            else:
                K = int('str')
            break
        except:
            print('Wrong!')
            continue

def flo(point):
    while True:
        try:
            print('Enter the',point,'point:',end = '')
            K = float(input())
            return K
        except:
            print('Wrong!')
            continue

fun = input('function')
while fun != 'sin' and fun != 'cos' and fun != 'tan':
    fun = input('right:')

a = flo('left')
b = flo('right')
n = pos_int()
result = 0.0

for i in range(1,n):
    result += ((b-a)/n)*getattr(math,fun)(a+(b-a)*(i-0.5)/n) #getattr() 将输入字符转变为函数
    
print(result)
