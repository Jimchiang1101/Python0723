id = 'A123456789'
sex = id[1] #1: 男生, 2: 女生
{
    '1':lambda :print('boy'),
    '2':lambda :print('girl')
}.get('1')