n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
A.sort()
B.sort()

for i in range(n):
    if A[i] == B[i]:
        if i == n - 1:
            print('Yes')

    else:
        print('No')
        break

