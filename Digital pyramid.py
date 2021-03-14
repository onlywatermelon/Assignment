def pos_int():
    while True:
        try:
            K = int(input('Enter the integer:'))
            if K > 0:
                return K
            else:
                K = int('str')
            break
        except:
            print('Wrong!')
            continue
N = pos_int()
for i in range(N):
    print('m\tm+1\tm**(m+1)')
    p = i+1
    print(p,p+1,p**(p+1),sep='\t')
