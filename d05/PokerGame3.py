import random
import time

def getScore(p):
    if p == 'A':
        return 1
    elif p == 'J' or p == 'Q' or p == 'K':
        return 0.5
    return p

pokerAmount = 6;
poker = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'] * 4
random.shuffle(poker)# 洗牌
#餘額(目前金額)
balance = 100

while True:
    #下注
    bet = int(input('請下注(不可超過 %d), 離開:-1: ' % balance))
    if bet == -1:
        print('User 目前餘額: ', balance)
        break
    if bet > balance:
        print('下注金額過大,請重新下注!User 目前餘額: ', balance)
        break
    #牌局開始先發一張
    p1 = poker.pop()
    sum = getScore(p1)
    print('User已拿:', p1, '總分', sum)


    #繼續拿牌 ?
    count_user = 0;
    # 進入User單局迴圈
    #.pop()從最尾端拿一張牌
    while True:
        ask = input('是否要拿牌(y/n)?')
        if ask == 'y':
            p = poker.pop()
            sum = sum + getScore(p)
            print('再拿',  p, '總分', sum)
            if sum > 10.5:
                print('User爆了')
                break
            else:
                count_user += 1
            if count_user == 5:
                print('User 過五關, 超強的~~~')
                break
        else:
            break

    #PC 拿牌
    count_pc = 0
    p2 = poker.pop()
    sum2 = getScore(p2)
    print('PC已拿:', p2, '總分', sum2)
    #進入PC單局迴圈
    while True:
        take = False #是否拿牌?
        time.sleep(5)  # 延遲 2 秒
        if sum2 >= 9:  #電腦若為9點(含)以上不須補牌
            break
        elif sum2 < 7: #若電腦少於7點強迫補牌
             p = poker.pop()
             sum2 = sum2 + getScore(p)
             print('PC再拿', p, '總分', sum2)
        elif sum2 == 7 or sum2 == 7.5:
            amount = poker.count('A') + poker.count(2) + poker.count(3)
            if amount >= 10 * pokerAmount:
                take = True
        elif  sum2 == 8 or sum2 == 8.5:
            amount = poker.count('A') + poker.count(2)
            if amount >= 7 * pokerAmount:
                teke = True
        # 是否拿牌 ?
        if take:
            p = poker.pop()
            sum2 += getScore(p)
            print('PC再拿:', p, '總分:', sum2)
        #是否爆了?
        if sum2 > 10.5:
            print('PC 爆了')
            break
        else:
            count_pc += 1

        #判斷是否過五關
        if count_pc == 5:
            print('PC 過五關, 超強的~~~')
            break
    # 判斷輸贏
    #sum, count_user
    #sum2, count_pc
    if count_user == 5 and sum <= 10.5:
        balance += bet
        print('User 贏, 最新餘額: ', balance)
        continue #進入下一局
    if (sum <= 10.5) and (sum2 > 10.5):
        balance +=bet
        print('User 贏, 最新餘額: ', balance)
        continue
    if(sum > sum2) and (sum <= 10.5):
        balance += bet
        print('User 贏, 最新餘額: ', balance)
        continue
    if (sum > 10.5 and sum2 > 10.5) or(sum == sum2):
        print('和局, 最新餘額: ', balance)
        continue
    balance -= bet
    print('PC 贏, User最新餘額: ', balance)
    continue