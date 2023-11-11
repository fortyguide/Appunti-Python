items = {'latte':3, 'riso':2, 'tofu':5}
print(items) 

item = items["latte"]
print(item)

items["latte"] = 2
item = items["latte"]
print(item)

items["cereali"] = 1
print(items)

items['yogurt'] = {'fragola':8, 'bianco':3}
print(items)
item = items['yogurt']['fragola']
print(item)

print(items.keys())

print(items.values())