n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
answer = []

for i in range(1, n+1, 2):
    new_arr = sorted(arr[:i])
    answer.append(new_arr[i//2])

print(*answer)

    