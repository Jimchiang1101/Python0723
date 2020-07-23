import random  #取得亂數


while True:
    n = random.randint(1, 100)
    if n % 13 ==0:
        print(n)
        continue

    #若 n 等於11的倍數就停止(break)
    if n % 11 == 0:
        break
