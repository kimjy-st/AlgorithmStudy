import sys
from io import StringIO


sys.stdin = StringIO('''2
15
1 2 3 3 1 3 2 4 1 1 3 1 3 3 1
18
1 2 3 1 2 3 1 2 3 3 3 3 2 2 2 1 1 1''')

T = int(sys.stdin.readline())

cases = []
for _ in range(T):
    n = int(sys.stdin.readline()) 
    arr = list(map(int, sys.stdin.readline().split()))
    cases.append(arr)


for case in cases:
    team_mem = {} # Team별 멤버 수 기록 
    team_score = {} # Team별 점수 기록

    # Init
    max_team_idx = max(case)
    for i in range(1, max_team_idx+1):
        mems = list(filter(lambda x: case[x] == i, range(len(case))))
        team_mem[i] = len(mems)
        if len(mems) >= 6:
            team_score[i] = []

    score = 1
    for t in case:
        if team_mem[t] >=6:
            team_score[t].append(score)
            score += 1
    
    win_idx, win_score = 0, 1e9
    
    for k, v in team_score.items():
        total_score = sum(v[:4])
        if win_score > total_score :
            win_idx = k
            win_score = total_score

        elif win_score == total_score and team_score[win_idx][4] > team_score[k][4]:
            win_idx = k
            win_score = total_score
    print(win_idx)
    


