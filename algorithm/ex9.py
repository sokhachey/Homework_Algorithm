# EX9.Create function to find average of price
# products = [
#     {"name": "Apple", "price": 20},
#     {"name": "Orange", "price": 24},
# ]
def average(array):
    average = 0
    for product in array:  
        if "price" in product:  
            average += product["price"]/2 
    return average
products = [
    {"name": "Apple", "price": 20},
    {"name": "Orange", "price": 24},
]
print(average(products))