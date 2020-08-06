#透過裝飾來檢核參數
def comfirm(func):
    def inner(a, b):
        if b == 0:
            print('分母不可 = 0')
            return 0
        return  func(a, b)
    return inner



@comfirm
def div(a, b):
    return a / b

if __name__ == '__main__':
    print(div(10, 2))
    print(div(10, 0))