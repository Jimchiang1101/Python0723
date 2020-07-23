def getSum(scores):
    sum = 0
    for i in range(0, len(scores)):
        sum += scores[i]  # 累加
        return sum
#主程式
scores = [100, 97, 80, 70, 60] #數組
for i in range(0, len(scores)):
    print(scores[i])
#求總分?
sum = 0
for i in range(0, len(scores)):
    sum += scores[i]  #累加
    print("總分: %d " % sum)

#求平均
avg = sum/ len(scores)
print('平均: %.1f' % avg)

