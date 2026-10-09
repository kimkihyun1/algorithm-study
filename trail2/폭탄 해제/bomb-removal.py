unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.
class Bomb:
    def __init__(self, code="", color="", second=0):
        self.code = code
        self.color = color
        self.second = second

bomb1 = Bomb(unlock_code, wire_color, seconds)
print(f"code : {bomb1.code}")
print(f"color : {bomb1.color}")
print(f"second : {bomb1.second}")
