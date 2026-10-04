n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
str.sort()
start_ap = []

for i in range(n):
    if str[i][:len(t)] == t:
        start_ap.append(str[i])

print(start_ap[k-1])