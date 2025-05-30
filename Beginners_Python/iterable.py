user = {
    'name' : 'golem',
    'age' : 50032,
    'can_swim' : False
}

for item in user.items():
    print(item)
    
for item in user.values():
    print(item)
    
for item in user.keys():
    print(item)

for key, value in user.items():
    print(key, value)
       