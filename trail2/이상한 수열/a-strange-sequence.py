N = int(input())

# Please write your code here.
def rec(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    return rec(n//3) + rec(n-1)

print(rec(N))