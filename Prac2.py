sales_data = {
    "Store_A": {
        "Laptop": 15,
        "Phone": 30,
        "Tablet": 10
    },
    "Store_B": {
        "Laptop": 25,
        "Phone": 20,
        "Tablet": 15
    },
    "Store_C": {
        "Laptop": 10,
        "Phone": 35,
        "Tablet": 5
    }
}

# Find the total sales for each product across all stores.
total_sales={}
for store in sales_data.values():
    for product, quantity in store.items():
        total_sales[product] = total_sales.get(product,0) + quantity
print(total_sales)

# Identify the store with the highest total sales (sum of all products) with units.
store = max(sales_data, key=lambda x: sum(sales_data[x].values()))
print(f"store with highest total sales: {store} : {sum(sales_data[store].values())} units")

# Find the best-selling product (i.e., the product with the highest total sales).
best_selling_product = max(total_sales, key=total_sales.get)
print(f"best selling product: {best_selling_product} : {total_sales[best_selling_product]} units")

# Sort the stores based on their total sales in descending order and print the sorted result.
sorted_stores = sorted(sales_data.items(), key=lambda x: sum(x[1].values()), reverse=True)
print(f"stores sorted by total sales in descending order: {sorted_stores}")