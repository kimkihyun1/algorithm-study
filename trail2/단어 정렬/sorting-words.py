n = int(input())
word = [input() for _ in range(n)]

# Please write your code here.
ans = sorted(word)
for i in range(n):
    print(ans[i])