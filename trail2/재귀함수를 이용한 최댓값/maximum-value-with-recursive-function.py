n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def max_num(num):
    if num == 0:
        return arr[0]

    return max(max_num(num - 1), arr[num])

print(max_num(n - 1))