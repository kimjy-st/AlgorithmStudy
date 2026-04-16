import sys
from io import StringIO

sys.stdin = StringIO('''3
4
7
10''')

T = int(sys.stdin.readline().strip())

cases = list(int(sys.stdin.readline().strip()) for _ in range(T))

keys = [1,2,3]
for case in cases:
    dp = [0 for _ in range(case+1)]
    dp[0] = 1
    answer = 0 
    for num in keys:
        for i in range(num, case + 1):
            dp[i] += dp[i-num]

    print(dp[-1])



    