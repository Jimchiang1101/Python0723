def calc(x, y ):
    a = 2*x
    b = y-a
    r = b/2
    c = x-r
    return  c, r
chicken,rabbit = calc(83, 240)
print("雞:%d 兔:%d 隻數:%d 腳數:%d " %
      (chicken, rabbit, chicken+rabbit,(chicken*2+rabbit*4) ))