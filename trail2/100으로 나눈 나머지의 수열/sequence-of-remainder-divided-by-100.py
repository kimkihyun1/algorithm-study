N = int(input())

# Please write your code here.
def rec(n):
    if n == 1:
        return 2
    if n == 2:
        return 4 

    return rec(n-1) * rec(n-2) % 100  

print(rec(N))