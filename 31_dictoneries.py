# ordered collection
dic={
    "name": "ayush",
    # ^^^^^    ^^^^^^
    # key      value 
    "age": 18
}
print(dic)
print(type(dic))
print(dic["name"])
print(dic.get("age"))

roll={
    121: "chanpu",
    122: "ghanpu",
    123: "banpu",
    124: "tanpu",
    125: "panpu",
    126: "manpu",
}
print(roll)
print(roll[122])
print(roll.get(122))
# print(roll[999])   # error
print(roll.get(999)) # to avoid error 

for key in roll:
    print(roll[key])

for key in roll.keys():
    print(f'value corrosponding to the {key} is {roll[key]}')

print(roll.items())
for key,value in roll.items():
    print(f'value corrosponding to the {key} is {value}')