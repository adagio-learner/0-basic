#check for repeatation in list:
# 1)Remove repeted element from list and print list. 
# 2)print repeated element list.
some_list = ['a', 'b', 'c', 'b', 'n', 'd', 'm', 'n', 'n']

repeated_element = []

for item in some_list:
    x = some_list.count(item)
    while x > 1:
        some_list.remove(item)
        x -= 1
        repeated_element.append(item)
print(f'non-repeated list = {some_list}')
print(f'repeated element = {repeated_element}')
for element in repeated_element:
    print(repeated_element.count(element))