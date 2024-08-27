# EX8.Create function to sum total of price 
# products = [
#     {"name": "Apple", "price": 20},
#     {"name": "Orange", "price": 24},
# ]
def sum_total(array):
    sum_total = 0
    for product in array:  
        if "price" in product:  
            sum_total += product["price"]  
    return sum_total
products = [
    {"name": "Apple", "price": 20},
    {"name": "Orange", "price": 24},
]
print(sum_total(products))