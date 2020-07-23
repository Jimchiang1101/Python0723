report = '台積電目前價格每股300元,非常適合買進'
amount = 1000 #想買1000 股(一張)
cost = 0 #請算出買進成本
price = report[9:12]
print(price, type(price))
cost = amount * int(price)
print(cost)