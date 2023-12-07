from testing.tests import all_tests, test_a, test_b, test_c, test_d, test_efgh, test_i, test_j


# FIXME

def map_input(input_value):
    match input_value:
        case 'a':
            return test_a.Test()
        case 'b':
            return test_b.Test()
        case 'c':
            return test_c.Test()
        case 'd':
            return test_d.Test()
        case 'e':
            return test_efgh.Test()
        case 'f':
            return test_efgh.Test()
        case 'g':
            return test_efgh.Test()
        case 'h':
            return test_efgh.Test()
        case 'i':
            return test_i.Test()
        case 'j':
            return test_j.Test()
        case 'all':
            return all_tests.All_tests()
        case _:
            print("Wrong input")
            return None


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

test = map_input(user_response)
test.setup_method()
test.test()
test.teardown_method()
