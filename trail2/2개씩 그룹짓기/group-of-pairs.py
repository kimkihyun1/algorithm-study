n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
answer = 0
nums.sort()

for i in range(n):
    value = nums[i] + nums[2*n - i - 1]

    if value > answer:
        answer = value

print(answer)