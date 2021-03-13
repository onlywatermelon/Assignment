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
        
n = pos_int()
prime_number_list = [i for i in range(2, n+1) if all(i % j != 0 for j in range(2, int(math.sqrt(i)) + 1))]
print('The prime numbers smaller than',n,'include:')
i = 0
for prime_number in prime_number_list:
    print(prime_number,'\t',end = '')
    i += 1
    if i % 8 == 0:
        print()
