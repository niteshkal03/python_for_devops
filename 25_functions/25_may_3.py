def solution(N):
    c=0
    for i in range(1,N+1):
        if i%2!=0:
            c+=i
    return c
print(solution(7))
