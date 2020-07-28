def f2c(f):
    c = (f - 32 ) * 5 / 9
    return c
def c2f(c):
    f = c * (9/5) +32
    return f
degree = float(input("請輸入溫度: "))
conversion = int(input("1.攝氏 -> 華氏. 2.華氏 ->攝氏"))
if conversion == 1:
    f = c2f(degree)
    print('%d 攝氏 = %d 華氏' %(degree, f))
elif conversion == 2:
    c = f2c(degree)
    print('%d 華氏 = %d 攝氏' % (degree, c))