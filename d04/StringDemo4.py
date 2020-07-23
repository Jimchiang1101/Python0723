report = '台積電目前價格每股350元,非常適合賣出4000股,目前我的庫存有6000股'
#求賣出後的庫存總值
a = float(report[9:12])
b = int(report[20:24])
c = int(report[33:37])
cost = (int(c) - int(b)) * int(a)
print(a, b, c,)
print(cost)