N = int(input())

# Please write your code here.
def print_sum(n):
    if n < 10:
        return n ** 2
    
    return print_sum(n // 10) + ((n % 10) ** 2)

print(print_sum(N))

    