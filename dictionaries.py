# key: value
# Dictionary items are ordered, changeable, and does not allow duplicates.

# dict() constructor
print(dict(name = "Z", age = 21, country = "Turkey")) # {'name': 'Z', 'age': 21, 'country': 'Turkey'}

fordmustang_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1970,
  "year": 2023 # overwrite existing value
}

print(fordmustang_dict["brand"]) # Ford

# .get()
print(fordmustang_dict.get("brand")) # Ford

# .keys()
print(fordmustang_dict.keys()) # dict_keys(['brand', 'model', 'year'])

# .values()
print(fordmustang_dict.values()) # dict_values(['Ford', 'Mustang', 2023])

# .items()
print(fordmustang_dict.items()) # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2023)])

for x, y in fordmustang_dict.items():
  print(x, y)
"""
brand Ford
model Mustang
year 2023
"""

# .setdefault()
print(fordmustang_dict.setdefault("year", 1970)) # 2023
# If the key does not exist, insert the key with the specified value.

# .update()
fordmustang_dict.update({"price": "$35.000"})
print(fordmustang_dict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 2023, 'price': '$35.000'}

# .pop()
print(fordmustang_dict.pop("brand")) # Ford
print(fordmustang_dict) # {'model': 'Mustang', 'year': 2023, 'price': '$35.000'}

#.popitem()
print(fordmustang_dict.popitem()) # ('price', '$35.000')
print(fordmustang_dict) # {'model': 'Mustang', 'year': 2023}

# del keyword
del fordmustang_dict["year"]
print(fordmustang_dict) # {'model': 'Mustang'}

fordmustang_dict.clear()
del fordmustang_dict

# .fromkeys()
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict) # {'key1': 0, 'key2': 0, 'key3': 0}

# zip()
keys = ['name', 'age']
values = ['Zeynep', 21]
d = {}
for k, v in zip(keys, values):
  d[k] = v
print(d) # {'name': 'Zeynep', 'age': 21}
