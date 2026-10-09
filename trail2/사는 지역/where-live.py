n = int(input())
name = []
address = []
region = []

for _ in range(n):
    name_value, address_value, region_value = input().split()
    name.append(name_value)
    address.append(address_value)
    region.append(region_value)

# Please write your code here.
class Info:
    def __init__(self, name="", address="", region=""):
        self.name = name
        self.address = address
        self.region = region

total = []

for i in range(n): 
    total.append(Info(name[i], address[i], region[i]))

last_idx = 0
for i, info in enumerate(total):
    if info.name > total[last_idx].name:
        last_idx = i

print(f"name {total[last_idx].name}")
print(f"addr {total[last_idx].address}")
print(f"city {total[last_idx].region}")
