# JavaScript object notation
import json

# JSON to Python - json.loads() - The result will be a dictionary.

json_string = '{"name":"Zeynep", "age":21, "city":"Istanbul"}'
python_dict = json.loads(json_string)

# Python to JSON - json.dumps()
python_dict = {
  "name": "Zeynep",
  "age": 21,
  "city": "Istanbul"
}
json_string = json.dumps(python_dict)

print(json.dumps(["a", "b"])) # ["a", "b"]
print(json.dumps(("a", "b"))) # ["a", "b"]
print(json.dumps(True)) # true
print(json.dumps(False)) # false
print(json.dumps(None)) # null

# dict - Object
# list & tuple - Array
# str - String, int & float - Number

person_python = {
  "name": "Elif",
  "age": 32,
  "married": True,
  "divorced": False,
  "children": ("Ali", "Ahmet"),
  "pets": None,
  "cars": [
    {"model": "Hyundai i10", "mpg": 35.4},
    {"model": "Honda Jazz", "mpg": 52.5}
  ]
}

print(json.dumps(person_python, indent=4, sort_keys=True))
# default value - separators=(", ", ": ")
"""
{
    "age": 32,
    "cars": [
        {
            "model": "Hyundai i10",
            "mpg": 35.4
        },
        {
            "model": "Honda Jazz",
            "mpg": 52.5
        }
    ],
    "children": [
        "Ali",
        "Ahmet"
    ],
    "divorced": false,
    "married": true,
    "name": "Elif",
    "pets": null
}
"""