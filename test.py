"""Este módulo contiene las pruebas unitarias para la aplicación de comercio electrónico."""

import functions

# Test for check_number_status
assert functions.check_number_status(1) == "Positive"
assert functions.check_number_status(0) == "Zero"
assert functions.check_number_status(-1) == "Negative"

# Test for calculate_total_discount
assert functions.calculate_total_discount(100) == 10
assert functions.calculate_total_discount(99) == 0
#assert functions.calculate_total_discount(101) == 10.1
assert functions.calculate_total_discount(500) == 50
assert functions.calculate_total_discount(501) == 100.2

# Test for calculate_items_shipping_cost
# Test for "standard" shipping
assert functions.calculate_items_shipping_cost([{'weight': 1}], "standard") == 10
assert functions.calculate_items_shipping_cost([{'weight': 5}], "standard") == 10
assert functions.calculate_items_shipping_cost([{'weight': 6}], "standard") == 15
assert functions.calculate_items_shipping_cost([{'weight': 10}], "standard") == 15
assert functions.calculate_items_shipping_cost([{'weight': 11}], "standard") == 20
# Test for "express" shipping
assert functions.calculate_items_shipping_cost([{'weight': 1}], "express") == 20
assert functions.calculate_items_shipping_cost([{'weight': 5}], "express") == 20
assert functions.calculate_items_shipping_cost([{'weight': 6}], "express") == 30
assert functions.calculate_items_shipping_cost([{'weight': 10}], "express") == 30
assert functions.calculate_items_shipping_cost([{'weight': 11}], "express") == 40

# Test for verify_age
assert functions.verify_age(17) == "Not Eligible"
assert functions.verify_age(18) == "Eligible"
assert functions.verify_age(65) == "Eligible"
assert functions.verify_age(66) == "Not Eligible"
