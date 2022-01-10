#dictionary stores element in a key, value pair
#unordered till python 3.6, after python 3.6 it is ordered

dict_products = {"shirt": 500, "t-shirt": 1000, "t-shirt": 700}
print(dict_products)
print(dict_products["t-shirt"])
print(dict_products.items())
print(dict_products.keys())
print(dict_products.values())

dict_products["t-shirt"] = 900
print(dict_products)

del dict_products["t-shirt"]
print(dict_products)
