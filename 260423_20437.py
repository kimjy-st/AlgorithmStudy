import sys
from io import StringIO
 

sys.stdin = StringIO('''2
superaquatornado
2
abcdefghijklmnopqrstuvwxyz
5''')

T = int(sys.stdin.readline())
words = []
Ks = []
for t in range(T):
    words.append(sys.stdin.readline().strip())
    Ks.append(int(sys.stdin.readline()))


# 각 문자가 등장하는 인덱스 기록 
for word, k in zip(words, Ks):
    dicts = {}
    min_len = 1e9
    max_len= -1 

    # 각 문자가 등장하는 인덱스 기록 
    for idx, w in enumerate(word):
        if w in dicts.keys():
            dicts[w].append(idx)
        else:
            dicts[w] = [idx]


     
    for w in dicts.keys():
        indices = dicts[w]

        # idx가 k개 이상일 때만 길이 체크
        if len(indices) < k:
            continue
        
        # k sliding window
        for i in range(len(indices) -k + 1):
            s = indices[i]
            e = indices[i+k -1]

            length = e-s + 1 

            min_len = min(min_len, length)
            max_len = max(max_len, length)

    if max_len == -1:
        print(-1)
    else:
        print(min_len, max_len)
