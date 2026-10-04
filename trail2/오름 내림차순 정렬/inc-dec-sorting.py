n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums = sorted(nums)
print(*nums)

nums = sorted(nums, reverse=True)
print(*nums)