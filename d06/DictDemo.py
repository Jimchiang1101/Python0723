fruits = {'orange':20, 'apple':10, 'watermelon':30}
print('orange 幾元', fruits.get('orange'))
print('apple 幾元', fruits.get('apple'))
print('watermelon 幾元', fruits.get('watermelon'))
print('banana 幾元',fruits.get('banana'))
print(fruits)
#setdefault(key值, 預設值(若找不到此元素))
print('banana 幾元',fruits.setdefault('banana', 70))
print(fruits)
#取得所有的key值
names = fruits.keys()
print(names, type(names))
value = fruits.values()
print(value, type(value), sum(value))