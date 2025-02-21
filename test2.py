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
# # Calculate total sales per product
# total_sales_per_product = {}
# for store in sales_data.values():
#     for product, quantity in store.items():
#         total_sales_per_product[product] = total_sales_per_product.get(product, 0) + quantity
#
# # Identify the store with the highest total sales
# store_sales = {store: sum(products.values()) for store, products in sales_data.items()}
# store_with_highest_sales = max(store_sales, key=store_sales.get)
#
# # Identify the best-selling product
# best_selling_product = max(total_sales_per_product, key=total_sales_per_product.get)
#
# # Sort stores based on total sales in descending order
# sorted_stores = sorted(store_sales.items(), key=lambda x: x[1], reverse=True)
#
# # Print results
# print("------------------------")
# print("\nTotal Sales Per Product:")
# for product, total in total_sales_per_product.items():
#     print(f"{product}: {total}")
#
# print(f"\nStore with Highest Total Sales: {store_with_highest_sales} ({store_sales[store_with_highest_sales]} units)")
#
# print(f"\nBest-Selling Product: {best_selling_product} ({total_sales_per_product[best_selling_product]} units)")
#
# print("\nStores Sorted by Total Sales:")
# for rank, (store, sales) in enumerate(sorted_stores, 1):
#     print(f"{rank}. {store} - {sales} units")
#
# // Functions Based --------------------------------------------------------------------------------------------------------------------------------------------
def calculate_total_sales(sales_data):
    """Calculate total sales for each product across all stores."""
    total_sales_per_product = {}
    for store in sales_data.values():
        for product, quantity in store.items():
            total_sales_per_product[product] = total_sales_per_product.get(product, 0) + quantity
    return total_sales_per_product

def get_store_sales(sales_data):
    """Calculate total sales for each store."""
    return {store: sum(products.values()) for store, products in sales_data.items()}

def get_highest_selling_store(store_sales):
    """Find the store with the highest total sales."""
    return max(store_sales, key=store_sales.get)

def get_best_selling_product(total_sales_per_product):
    """Find the product with the highest total sales."""
    return max(total_sales_per_product, key=total_sales_per_product.get)

def sort_stores_by_sales(store_sales):
    """Sort stores by total sales in descending order."""
    return sorted(store_sales.items(), key=lambda x: x[1], reverse=True)

def print_results(total_sales_per_product, store_sales, highest_store, best_product, sorted_stores):
    """Prints the results in a formatted manner."""
    print("------------------------")
    print("\nTotal Sales Per Product:")
    for product, total in total_sales_per_product.items():
        print(f"{product}: {total}")

    print(f"\nStore with Highest Total Sales: {highest_store} ({store_sales[highest_store]} units)")

    print(f"\nBest-Selling Product: {best_product} ({total_sales_per_product[best_product]} units)")

    print("\nStores Sorted by Total Sales:")
    for rank, (store, sales) in enumerate(sorted_stores, 1):
        print(f"{rank}. {store} - {sales} units")

# Main Execution
sales_data = {
    "Store_A": {"Laptop": 15, "Phone": 30, "Tablet": 10},
    "Store_B": {"Laptop": 25, "Phone": 20, "Tablet": 15},
    "Store_C": {"Laptop": 10, "Phone": 35, "Tablet": 5}
}

# Process the sales data
total_sales_per_product = calculate_total_sales(sales_data)
store_sales = get_store_sales(sales_data)
highest_store = get_highest_selling_store(store_sales)
best_product = get_best_selling_product(total_sales_per_product)
sorted_stores = sort_stores_by_sales(store_sales)

# Print the results
print_results(total_sales_per_product, store_sales, highest_store, best_product, sorted_stores)

