# A set is a collection which is unordered, unchangeable, and unindexed. But you can remove items and add new items.
# Sets do not allow duplicate values.

cars_set = {"Mercedes", "BMW", "Honda", "BMW", "BMW"}
print(cars_set) # {'Mercedes', 'Honda', 'BMW'}

print(len(cars_set)) # 3

# .add()
cars_set.add("Maserati")
print(cars_set) # {'BMW', 'Honda', 'Mercedes', 'Maserati'}

# .update() - sets, tuples, lists, dictionaries etc.
cars_set_update = {"Ferrari", "Porsche"}
cars_set.update(cars_set_update)
print(cars_set) # {'Porsche', 'Maserati', 'Ferrari', 'Mercedes', 'Honda', 'BMW'}

# .remove() - If the item to remove does not exist, remove() will raise an error.
cars_set.remove("BMW")
print(cars_set) # {'Porsche', 'Maserati', 'Honda', 'Ferrari', 'Mercedes'}

# .discard() - If the item to remove does not exist, discard() will NOT raise an error.
cars_set.discard("Honda")
print(cars_set) # {'Porsche', 'Maserati', 'Ferrari', 'Mercedes'}

# .pop() - Remove a random item
cars_set.pop()
print(cars_set) # {'Maserati', 'Ferrari', 'Mercedes'}

cars_set.clear()
del cars_set

set1 = {1, 2, 3, 8, 10}
set2 = {4, 5, 6, 8, 10}

# .union()
print(set1.union(set2)) # {1, 2, 3, 4, 5, 6, 8, 10}

# .intersection()
print(set1.intersection(set2)) # {8, 10}

# .symmetric_difference()
print(set1.symmetric_difference(set2)) # {1, 2, 3, 4, 5, 6}

# .difference()
print(set1.difference(set2)) # {1, 2, 3}
print(set2.difference(set1)) # {4, 5, 6}

# .isdisjoint()
print(set1.isdisjoint(set2)) # False - they have a intersection

# .issubset()
print(set1.issubset(set2)) # False
# .issuperset()
print(set1.issuperset(set2)) # False
