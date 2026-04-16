import sys
from io import StringIO 
from collections import defaultdict
sys.stdin = StringIO('''12 5
appearance
append
attendance
swim
swift
swift
swift
mouse
wallet
mouse
ice
age''')

N, M = map(int, sys.stdin.readline().split(' '))

words = [sys.stdin.readline().strip() for _ in range(N)]


# 조건 순위 
# M보다 길이가 긴 단어일 것 
# 자주 나온 단어일 것 
# 해당 단어의 길이가 길수록 앞에 배치할 것 
# 같은 길이일 때 앞에 있는 단어가 오도록 할 것 

info = defaultdict(int)
for word in words:
    if len(word) >= M:
        info[word] += 1

answer = list(info.keys())
answer.sort(key=lambda x:(-info[x], -len(x), x))

for word in answer:
    print(word)