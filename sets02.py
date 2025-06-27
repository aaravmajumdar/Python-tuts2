# sets1 = {"Rahul", 18, 'cse'}
# sets2 = {"Neha", 18, 'ece'}

# # sets3 = sets1.intersection(sets2)
# print(sets1.isdisjoint(sets2))

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid", "Kabul"}
print(cities.issuperset(cities3))
cities4 = { "Madrid" }
print(cities.issuperset(cities4))
