MAX_N = 5

users = []
for _ in range(MAX_N):
    codename, score = input().split()
    users.append((codename, int(score)))

# Please write your code here.
answer = float('inf')

for i in range(MAX_N):
    if answer > users[i][1]:
        answer = users[i][1]
        name = users[i][0]

print(name, answer)

    