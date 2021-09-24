items=['fruits','books','others']
keys=[55,66,99]

d={item.upper():price   for item ,price in zip(items,keys)}
print(d)
print(type(d))