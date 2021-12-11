# Using the built-in 'zip()' function.

days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri')
fruits = ['banana', 'orange', 'kiwi', 'apple']
drinks = ('coffee', 'tea', 'water', 'milk')
desserts = ['cake', 'ice cream', 'pie', 'milk shake']

# 'zip' combines datasets together
# 'zip' stops when the shortest collection runs out of members
zipped_collection = zip(days, fruits, drinks, desserts)

# Iterate over the zipped collection
for day, fruit, drink, dessert in zipped_collection:
    print("On {0} I had {1} with {2} then {3}.".format(day, fruit, drink, dessert))
