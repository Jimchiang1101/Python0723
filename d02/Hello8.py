pen = 10
amount = 200
total = pen * amount
print(pen, amount, total)
print(pen, amount, total, sep="&")
print(pen, amount, total, sep=",")
#print('鉛筆每支15元200支總共是3000元')
print('鉛筆每支' + str(pen) + '元' + str(amount) + '支總共是' + str(total) + '元')
print('鉛筆每支%d元%d支總共是%d' %(pen, amount, total))