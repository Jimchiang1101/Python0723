def add(x):
    return x + 1

def sum(y):
    return y - 1

def operator(func, n):
    if (n < 200):
        n = 200
    return func(n)

if __name__ == '__main__':
    operator(add, 5)
    operator(sum, 5)