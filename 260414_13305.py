import sys
from io import StringIO


sys.stdin = StringIO('''4
3 3 4
1 1 1 1''')

N = int(sys.stdin.readline())
dist = list(map(int, sys.stdin.readline().split()))
fee = list(map(int, sys.stdin.readline().split()))

total_fee = 0
# 시작 지점에서 적어도 dist[0]만큼의 주유는 해야함
# 제일 요금이 적은데서 많이 사는 것이 유리함 
min_fee = fee[0]
for i in range(N-1):
    min_fee = min(min_fee, fee[i])
    total_fee += min_fee * dist[i]
print(total_fee)