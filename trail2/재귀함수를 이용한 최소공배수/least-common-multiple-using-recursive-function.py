n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)

def lcm(a, b):
    return a // gcd(a, b) * b

answer = 1

for num in arr:
    answer = lcm(answer, num)

print(answer)

