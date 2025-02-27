products = {
    "Laptop": 75000,
    "Phone": 50000,
    "Headphones": 3000,
    "Smartwatch": 12000,
    "Tablet": 35000
}

# 1)Sort the products based on price in ascending order.
# 2)Sort the products based on price in descending order.
# 3)Find the most expensive product.
# 4)Find the average price of all products.

# 1)
asc_products = sorted(products.items(),key = lambda x : x[1])
print(f"Products in ascending order : {asc_products}")

# 2)
des_products = sorted(products.items(),key = lambda x : x[1], reverse=True)
print(f"Products in descending order : {des_products}")

# 3)
most_expensive_product_price = max(products.values())
most_expensive_product = max(products, key=products.get)
print(f"Most expensive product : {most_expensive_product} : {most_expensive_product_price}")

# 4)
total = sum(products.values())

avg_price = total / len(products)
print(f"Average of all products is {avg_price}")