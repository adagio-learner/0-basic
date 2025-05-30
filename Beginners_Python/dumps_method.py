book = {}
book['tom'] = {
    'name' : 'tom',
    'address' : '1 red street, NY',
    'phone' : 98989898
}
book['bob'] = {
    'name' : 'bob',
    'address' : '1 green street, NY',
    'phone' : 90909090
}


import json
s = json.dumps(book)
with open('D:\PYTHON\pycharm\dumps_method.txt','w') as f:
    f.write(s)
book=json.loads(s)  #use for converting in books

for person in book:
    print(book[person])