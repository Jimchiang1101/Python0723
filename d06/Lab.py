n = int(input('輸入一個整數: '))
c = 2
while c < n:
    if n % c == 0:
        print('不是質數')
        break
    c += 1
if c == n:
    print('是質數')

#for迴圈
n = int(input('輸入一個正整數'))

for i in range(2,n):
    if n % c == 0:
        print('不是質數')
        break
    elif c == n-1:
        print('是質數')
if n == 2 :
    print('是質數')

#老師寫法
def isPrime(n):
    bool = True  # 假設是質數
    for i in range(2, n//2+1):  # begin(含), end(不含)
        if n % i == 0:
            bool = False
            break
    return bool

if '__main__' == __name__ :  #Python的主程式
    for n in range(2, 101):
        if isPrime(n):
            print(n)