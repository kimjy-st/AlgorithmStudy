import sys
from io import StringIO

sys.stdin = StringIO('''60000 101 891''')
R, M, S = map(int, sys.stdin.readline().split())
m_cur = M
s_cur = S
match = -1
for round in range(1, (R+1)//2 + 1):
    if abs(m_cur - s_cur) == 1 and min(m_cur, s_cur)% 2 == 1:
        match = round
        break
    else:
        m_cur = (m_cur + 1)//2
        s_cur = (s_cur + 1)//2



print(match)
