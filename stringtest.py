url = "/restaurants/1/edit"

urlSplit = url.split("/")

for i,val in enumerate(urlSplit):
    print i, val

info = {
    "age": 2
}

print info['age']

info['age'] = 22

print info.get('age')