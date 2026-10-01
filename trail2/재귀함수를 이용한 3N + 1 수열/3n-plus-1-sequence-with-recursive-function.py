n = int(input())

# Please write your code here.
def rec(n):
    global count
    
    if n == 1:
        return count

    count += 1

    if n % 2 == 0:
        return rec(n / 2)
    else:
        return rec(n * 3 + 1)

count = 0

print(rec(n))