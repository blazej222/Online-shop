script_list = ''' 
a) Adding 10 products with varying quantities
b) Search up a product and add a random one from the lot
c) Delete 3 products from the cart
d) Account registration
e, f, g, h) Ordering the cart content
i) Checking the status of an order
j) Downloading an invoice
'''

user_response = input('Select a script to run OR type "all" for the whole sequence: ' + script_list)
print(f'Selected script: {user_response}')

