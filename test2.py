# sales_data = {
#     "Store_A": {
#         "Laptop": 15,
#         "Phone": 30,
#         "Tablet": 10
#     },
#     "Store_B": {
#         "Laptop": 25,
#         "Phone": 20,
#         "Tablet": 15
#     },
#     "Store_C": {
#         "Laptop": 10,
#         "Phone": 35,
#         "Tablet": 5
#     }
# }
#
# # Find the total sales for each product across all stores.
# total_sales = {}
# for store, products in sales_data.items():
#     for product, sales in products.items():
#         if product in total_sales:
#             total_sales[product] += sales
#         else:
#             total_sales[product] = sales
#
#     # Find the best-selling product (i.e., the product with the highest total sales).
#     best_selling_product = max(total_sales, key=total_sales.get)
#     best_sales_value = total_sales[best_selling_product]
#
# print(f"The total sales for each product across all stores {total_sales}")
# print(f"The best-selling product is {best_selling_product} : {best_sales_value}")
#
# # Identify the store with the highest total sales (sum of all products).
# highest_sales_store = None
# highest_sales_total = 0
#
# for store, product in sales_data.items():
#     total_sales = sum(product.values())
#
#     if total_sales > highest_sales_total:
#         highest_sales_total = total_sales
#         highest_sales_store = store
#
# print(f"The store with the highest product sale {highest_sales_store} : {highest_sales_total}")
#
# # Sort the stores based on their total sales in descending order and print the sorted result.
# sorted_stores = sorted(sales_data.items(), key=lambda x: sum(x[1].values()), reverse=True)
# print(f"Stores sorted by total sales in descending order: {sorted_stores}")

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

# Calculate total sales per product
total_sales_per_product = {}
for store in sales_data.values():
    for product, quantity in store.items():
        total_sales_per_product[product] = total_sales_per_product.get(product, 0) + quantity

# Identify the store with the highest total sales
store_sales = {store: sum(products.values()) for store, products in sales_data.items()}
store_with_highest_sales = max(store_sales, key=store_sales.get)

# Identify the best-selling product
best_selling_product = max(total_sales_per_product, key=total_sales_per_product.get)

# Sort stores based on total sales in descending order
sorted_stores = sorted(store_sales.items(), key=lambda x: x[1], reverse=True)

# Print results
print("------------------------")
print("\nTotal Sales Per Product:")
for product, total in total_sales_per_product.items():
    print(f"{product}: {total}")

print(f"\nStore with Highest Total Sales: {store_with_highest_sales} ({store_sales[store_with_highest_sales]} units)")

print(f"\nBest-Selling Product: {best_selling_product} ({total_sales_per_product[best_selling_product]} units)")

print("\nStores Sorted by Total Sales:")
for rank, (store, sales) in enumerate(sorted_stores, 1):
    print(f"{rank}. {store} - {sales} units")
