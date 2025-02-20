# def prepare_order_vals(order_no, customer, product, quantity, price):
#     subtotal = quantity * price
#     order_vals = {
#         'order_no': order_no,
#         'customer': customer,
#         'product': product,
#         'quantity': quantity,
#         'price': price,
#         'subtotal': subtotal
#     }
#     return order_vals
#
#
# def customer_order_count(order_data):
#     order_count = {}
#     for order in order_data:
#         customer_name = order['customer']
#         if order_count.get(customer_name):
#             order_count[customer_name] += 1
#         else:
#             order_count[customer_name] = 1
#
#     return order_count
#
# order_data = []
# need_stop = True
# while need_stop:
#
#     order_no = input('Enter order number: ')
#     customer = input('Enter customer name: ')
#     product_name = input('Enter product name: ')
#     quantity = int(input('Enter quantity: '))
#     price = float(input('Enter price: '))
#
#     # positional args
#     # order_vals = prepare_order_vals(order_no, customer, product_name, quantity, price)
#
#     #keyword args
#     order_vals = prepare_order_vals(customer=customer, product=product_name, quantity=quantity, price=price, order_no=order_no)
#
#     order_data.append(order_vals)
#     is_stop = input('Do you want to stop? (y/n): ')
#     if is_stop.lower() == 'y':
#         need_stop = False
#
# print("order_data==", order_data)
#
# # order count by customer
#
# order_count = customer_order_count(order_data)
#
# print("order_count====",order_count)

# *args, **kwargs

def test_args(*args):
    return sum(args)

total = test_args(10,20, 30)

print(total)

# kwargs
def test_kwargs(**kwargs):
    name = kwargs.get('name')
    print("name:",name)
    print(kwargs)

data = test_kwargs(name="alpesh", city="baroda")
print(data)
