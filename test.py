import functions

assert functions.check_number_status(1) == "Positive"
assert functions.check_number_status(0) == "Zero"
assert functions.check_number_status(-1) == "Negative"
