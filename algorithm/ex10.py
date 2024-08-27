# EX10.Show product name that has maximum price
# products = [
#     {"name": "Apple", "price": 20},
#     {"name": "Orange", "price": 24},
# ]
def max(array):
    max_product = array[0]
    for product in array[1:]:
       if product["price"] > max_product["price"]:
        max_product = product
    
    return max_product["name"]
products = [
    {"name": "Apple", "price": 20},
    {"name": "Orange", "price": 24},
]
print("name Price:",max(products))