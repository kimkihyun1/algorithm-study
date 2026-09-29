a, b, c = map(int, input().split())

# Please write your code here.
multi_num = a * b * c
answer = 0

def sum_num(n):
    if n < 10:
        return n
    
    return sum_num(n // 10) + n % 10 
    
print(sum_num(multi_num))