data = '170,60&160,48'
print(data,type(data))

list = data.split('&')
list2 = list[0].split(',')
list3 = list[1].split(',')
print(list, type(list))
print(list2, type(list2))
print(list3, type(list3))



#老師的方法
for row in data.split('&'):
    print(row, type(row))
    r = row.split(',')

    bmi = '%.2f' %(float(r[1])/(float(r[0])/100)**2)
    print(bmi)