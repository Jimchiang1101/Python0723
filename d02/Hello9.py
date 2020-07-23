#撰寫一個BMI 系統
#可以輸入人名 , 身高, 體重
#系統會算出BMI的結果
#資料呈現: 小明身高是170cm 體重是60 kg BMI 計算結果為20.76(正常)
print('BMI 系統')
n = input('請輸入姓名: ')
h = float(input('請輸入身高: '))
w = float(input('請輸入體重: '))
bmi = w / ((h/100)**2)
result = '正常' if 18 < bmi <= 23 else '過高' if bmi > 23 else '過低'
print('%s的身高是 %f cm 體重是 %f  kg BMI 計算結果為 %f (%s)'% (n, h, w, bmi, result))
