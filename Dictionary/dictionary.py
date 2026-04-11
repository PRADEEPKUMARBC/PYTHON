# Dictinary = a collection of { key : value} pairs
#  ordered and changeable. No Duplicates

capitals = {
    "USA": "Washington D C",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow"
}

print(dir(capitals))
print(help(capitals))
print(capitals.get("Japan"))

if capitals.get("Russia"):
    print("That capital exist")
else:
    print("That capital doesn't exist")

capitals.update({"Germany" : "Berlin"})
capitals.update({"USA":"Detroit"})
capitals.pop("China")

keys = capitals.keys()
for key in keys:
    print(key)
print()

values = capitals.values()
for value in values:
    print(value)

items = capitals.items()
for key, value in capitals.items():
    print(f"{key} : {value}")

print(capitals)