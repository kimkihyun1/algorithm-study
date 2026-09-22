N = int(input())
cnt = 0

# Please write your code here.
def print_cnt(n, cnt):
    

    if n == 1:
        return cnt

    if n % 2 == 0:
        cnt += 1
        return print_cnt(n // 2, cnt)

    else: 
        cnt += 1
        return print_cnt(n // 3, cnt)  

result = print_cnt(N, cnt)
print(result)