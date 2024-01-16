'''
Calculate the possible amount of staircases for a number N.
At least 2 steps, all steps from at least one brick and 
of different size.
N = 3
# 
##
Amount of options is 1.
N = 4
#
###
Amount of options is 1.
N = 5
#
####

##
###
2 options.

N = 200: 487067745 options.
The answer is base on:
S(N,K) = S(N-K, K-1) + S(N, K-1)
Where K is the max length of a step.
We need to calculate S(N, N-1).
'''
def solution(n):
    if not n or n < 3:  #2 steps min. are required which requires (1+2)=3 bricks
        return 0
    S = [0]*(n+1)
    S[0] = 1 
    for k in range(1, n):  # k for our Sk(N) 
        for j in range(n, k-1, -1):  # N for our Sk(N)
            S[j] += S[j-k]  
    return S[n]
n = 200
print(solution(n))