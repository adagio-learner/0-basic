my_list = [1,2,3]
print('A')
for item in my_list:
    print(item)
    continue

print('B')
my_list = [1,2,3]
for item in my_list:
    continue
    print(item)

print('C')
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    continue

print('D')
i = 0
while i < len(my_list):
    continue
    print(my_list[i])
    i += 1