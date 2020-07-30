def sort(key, rows):
    for i in range(0, len(rows)-1):
        for j in range(i + 1, len(rows)):
            x = rows[i]
            if rows[i].get(key) > rows[j].get(key):  # 排序欄位比較
                rows[i] = rows[j]
                rows[j] = x
    return rows

if __name__ == '__main__':


   rows = [{'age':10, 'score':70},
           {'age':40, 'score':80},
           {'age':25, 'score':100}]
   rows = sort('score', rows)
   print(rows)

