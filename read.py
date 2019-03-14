import time


# 讀取檔案並傳回，印出總數
def count(file_name):
    data = []
    count = 0
    with open(file_name, 'r') as f:
        for line in f:
            data.append(line)
            count += 1
            if count % 100000 == 0:
                print(len(data))
    print('檔案讀取完成，共有', len(data), '筆資料')
    return data

# 計算平均長度，印出並傳回
def ave_len(data):
    L = 0
    for review in data:
        L += len(review)
    L_avg = L / len(data)
    print('每筆留言平均長度為：', L_avg)
    return L_avg

# 篩選短於特定長度留言的數量並傳回，印出數量
def sr(data, l = 100):
    shorter_reviews = []
    for d in data:
        if len(d) < l:
            shorter_reviews.append(d)
    print('長度小於', l, '的留言數量:', len(shorter_reviews))
    return shorter_reviews

# 尋找包含特定字串的留言並傳回，印出數量
def word_search(data, word):
    include_word = []
    for d in data:
        if word in d:
            include_word.append(d)
    print('內容包含', word, '的留言數量:', len(include_word))
    return include_word


# 計算每個單字出現次數
def word_count(data):
    wc = {}
    for d in data:
        words = d.split()
        for word in words:
            if word not in wc:
                wc[word] = 1
            else :
                wc[word] += 1
    return wc

# 查找字典中的key
def count_search(dic):
    key = ''
    print('\nkey word 查尋功能。輸入「%quit」可結束')
    while key != '%quit':
        key = input('\n請輸入關鍵字：')
        if key in dic:
            print(dic[key])
        else:
            print(0)

# 篩選出現超過特定次數的字詞
def count_filter(dic):
    while True:
        cou = input('\n印出出現特定次數以上字詞，次數：')
        cou = int(cou)
        for word in dic:
            if dic[word] >= cou:
                print(word, dic[word])


data = count('reviews.txt')

wc = word_count(data)
count_search(wc)
count_filter(wc)

# ave_len(data)
# print(sr(data, 98)[0])
# print(word_search(data, ' good ')[0])