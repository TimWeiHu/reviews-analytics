data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 10000 == 0:
            print(len(data))
print('檔案讀取完成，共有', len(data), '筆資料')

L = 0
for review in data:
    L += len(review)
L_avg = L / len(data)
print('每筆留言平均長度為：', L_avg)
