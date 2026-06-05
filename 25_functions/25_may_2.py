def solution(N):
    s=1
    for i in range(1,N):
        s=s*i
    return s
print(solution(5))