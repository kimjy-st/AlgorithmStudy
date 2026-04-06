triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
answer = 30

def solution(triangle):
    dp = [[0]*len(floor) for floor in triangle]
    dp[0][0] = triangle[0][0]
    for i, floor in enumerate(triangle):
        if i-1 >= 0:
            for j in range(len(floor)):
                if j-1 < 0:
                    cost =  dp[i-1][0]+ floor[j]
                elif j > len(floor)-2:
                    cost = dp[i-1][j-1] + floor[j]
                else:
                    left = dp[i-1][j-1] + floor[j]
                    right = dp[i-1][j]+ floor[j]
                    cost = right if left < right else left

                if dp[i][j]<=cost :
                    dp[i][j] = cost 
            
    answer = max(dp[-1])
    return answer
