# Given a dictionary of sales data and another dictionary of product prices, calculate total revenue for each store.
# Identify which store generated the highest revenue.

sales_data = {
    "Store_A": {"Laptop": 15, "Phone": 30, "Tablet": 10},
    "Store_B": {"Laptop": 25, "Phone": 20, "Tablet": 15},
    "Store_C": {"Laptop": 10, "Phone": 35, "Tablet": 5}
}

product_prices = {
    "Laptop": 1000,
    "Phone": 500,
    "Tablet": 300
}

# Expected Output:
# Revenue per store: {'Store_A': 34500, 'Store_B': 37500, 'Store_C': 30500}
# Most profitable store: Store_B

def calculate_revenue(sales_data, product_prices):
    revenue_per_store = {}
    for item, quantity in sales_data.items():
        for product, price in quantity.items():
            revenue_per_store[item] = revenue_per_store.get(item, 0) + price * product_prices[product]
    return revenue_per_store

revenue_per_store =  calculate_revenue(sales_data, product_prices)
print(f"Revenue per store: {revenue_per_store}")
print(f"Most profitable store: {max(revenue_per_store, key=revenue_per_store.get)}")


