"""
 White-box unit testing examples.
 domi
"""
import unittest
from unittest import TestCase, mock
import io

from white_box_homework import *;



class TestCheckNumberStatus(unittest.TestCase):
    """
    White-box unittest class.
    """
    def test_check_number_status_positive(self):
        """
        Checks the number is positive.
        """
        self.assertEqual(check_number_status(1), "Positive")

    def test_check_number_status_negative(self):
        """
        Checks the number is negative.
        """
        self.assertEqual(check_number_status(-1), "Negative")

    def test_check_number_status_zero(self):
        """
        Checks the number is zero.
        """
        self.assertEqual(check_number_status(0), "Zero")

class Test_validate_password(unittest.TestCase):
    """
    White-box unittest class.
    """
    def test_validate_password_valid(self):
        """
        Checks the password is valid.
        """
        self.assertTrue(validate_password("Password123!"))

    def test_validate_password_invalid(self):
        """
        Checks the password is invalid no uppecase letter.
        """
        self.assertFalse(validate_password("password123!"))
        """
        Checks the password is invalid no lowercaseletter .
        """
        self.assertFalse(validate_password("PASSWORD123!"))
        """
        Checks the password is invalid no number.
        """
        self.assertFalse(validate_password("Password!"))
        """
        Checks the password is invalid no special character.
        """
        self.assertFalse(validate_password("Password123"))

class Test_calculate_total_discount(unittest.TestCase):
    """
    White-box unittest class.
    """
    def test_calculate_total_discount_no_discount(self):
        """
        Checks the discount is valid.
        """
        self.assertEqual(calculate_total_discount(99), 0)

    def test_calculate_total_discount_10_percent(self):
        """
        Checks the discount is valid 100<=amount<=500.
        """
        self.assertEqual(calculate_total_discount(100), 10)
        self.assertEqual(calculate_total_discount(101), 10.100000000000001)
        self.assertEqual(calculate_total_discount(500), 50)
        self.assertEqual(calculate_total_discount(499), 49.900000000000006)

    def test_calculate_total_discount_20_percent(self):
        """
        Checks the discount is valid 500<amount<=1000.
        """
        self.assertEqual(calculate_total_discount(501), 100.2)
        self.assertEqual(calculate_total_discount(1000), 200)


class TestCalculateOrderTotal(unittest.TestCase):
    """
    Tests for the calculate_order_total function.
    """

    def test_empty_order(self):
        """
        Test an empty order list.
        """
        items = []
        self.assertEqual(calculate_order_total(items), 0)

    def test_single_item_no_discount(self):
        """
        Test a single item with quantity 1-5.
        """
        items = [{"quantity": 3, "price": 10}]
        self.assertEqual(calculate_order_total(items), 30)

    def test_single_item_5_percent_discount(self):
        """
        Test a single item with quantity 6-10.
        """
        items = [{"quantity": 7, "price": 10}]
        self.assertEqual(calculate_order_total(items), 66.5)  # 7 * 10 * 0.95

    def test_single_item_10_percent_discount(self):
        """
        Test a single item with quantity >10.
        """
        items = [{"quantity": 12, "price": 10}]
        self.assertEqual(calculate_order_total(items), 108)  # 12 * 10 * 0.9

    def test_multiple_items_mixed_discounts(self):
        """
        Test multiple items with different quantities.
        """
        items = [{"quantity": 3, "price": 10}, {"quantity": 7, "price": 20}, {"quantity": 15, "price": 5}]
        # No discount for first item, 5% discount for second, 10% discount for third
        expected_total = (3 * 10) + (7 * 20 * 0.95) + (15 * 5 * 0.9)
        self.assertAlmostEqual(calculate_order_total(items), expected_total)

class TestCalculateItemsShippingCost(unittest.TestCase):
    """
    Tests for the calculate_items_shipping_cost function.
    """

    def test_standard_shipping_low_weight(self):
        """
        Test standard shipping cost for low weight items.
        """
        items = [{"weight": 2}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 10)

    def test_standard_shipping_medium_weight(self):
        """
        Test standard shipping cost for medium weight items.
        """
        items = [{"weight": 6}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 15)

    def test_standard_shipping_high_weight(self):
        """
        Test standard shipping cost for high weight items.
        """
        items = [{"weight": 11}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 20)

    def test_express_shipping_low_weight(self):
        """
        Test express shipping cost for low weight items.
        """
        items = [{"weight": 2}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 20)

    def test_express_shipping_medium_weight(self):
        """
        Test express shipping cost for medium weight items.
        """
        items = [{"weight": 6}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 30)

    def test_express_shipping_high_weight(self):
        """
        Test express shipping cost for high weight items.
        """
        items = [{"weight": 11}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 40)

    def test_invalid_shipping_method(self):
        """
        Test invalid shipping method.
        """
        items = [{"weight": 2}]
        with self.assertRaises(ValueError):
            calculate_items_shipping_cost(items, "overnight")

class TestValidateLogin(unittest.TestCase):
    """
    Tests for the validate_login function.
    """

    def test_valid_login(self):
        """
        Test a valid login.
        """
        self.assertEqual(validate_login("user123", "password123"), "Login Successful")

    def test_invalid_username_short(self):
        """
        Test an invalid username that is too short.
        """
        self.assertEqual(validate_login("usr", "password123"), "Login Failed")

    def test_invalid_username_long(self):
        """
        Test an invalid username that is too long.
        """
        self.assertEqual(validate_login("a" * 21, "password123"), "Login Failed")

    def test_invalid_password_short(self):
        """
        Test an invalid password that is too short.
        """
        self.assertEqual(validate_login("user123", "pass"), "Login Failed")

    def test_invalid_password_long(self):
        """
        Test an invalid password that is too long.
        """
        self.assertEqual(validate_login("user123", "p" * 16), "Login Failed")

class TestVerifyAge(unittest.TestCase):
    """
    Tests for the verify_age function.
    """

    def test_age_eligible(self):
        """
        Test an age that is eligible.
        """
        self.assertEqual(verify_age(25), "Eligible")

    def test_age_young(self):
        """
        Test an age that is too young.
        """
        self.assertEqual(verify_age(17), "Not Eligible")

    def test_age_old(self):
        """
        Test an age that is too old.
        """
        self.assertEqual(verify_age(66), "Not Eligible")

class TestCategorizeProduct(unittest.TestCase):
    """
    Class for testing the categorize_product function.
    """
    def test_category_a(self):
        """
        Test a product price in category A.
        """
        self.assertEqual(categorize_product(25), "Category A")

    def test_category_b(self):
        """
        Test a product price in category B.
        """
        self.assertEqual(categorize_product(75), "Category B")

    def test_category_c(self):
        """
        Test a product price in category C.
        """
        self.assertEqual(categorize_product(150), "Category C")

    def test_category_d(self):
        """
        Test a product price in category D.
        """
        self.assertEqual(categorize_product(250), "Category D")

class TestValidateEmail(unittest.TestCase):
    """
    Class for testing the validate_email function.
    """
    def test_valid_email(self):
        """
        Test a valid email address.
        """
        self.assertEqual(validate_email("test@example.com"), "Valid Email")

    def test_invalid_email_no_at(self):
        """
        Test an email address without an @ symbol.
        """
        self.assertEqual(validate_email("testexample.com"), "Invalid Email")

    def test_invalid_email_no_dot(self):
        """
        Test an email address without a dot.
        """
        self.assertEqual(validate_email("test@examplecom"), "Invalid Email")

    def test_invalid_email_too_short(self):
        """
        Test an email address that is too short.
        """
        self.assertEqual(validate_email("t@e.c"), "Valid Email")

    def test_invalid_email_too_long(self):
        """
        Test an email address that is too long.
        """
        self.assertEqual(validate_email("t" * 51 + "@example.com"), "Invalid Email")

class TestCelsiusToFahrenheit(unittest.TestCase):
    """
    Class for testing the celsius_to_fahrenheit function.
    """
    def test_valid_conversion(self):
        """
        Test a valid temperature conversion.
        """
        self.assertAlmostEqual(celsius_to_fahrenheit(25), 77)

    def test_invalid_temperature(self):
        """
        Test an invalid temperature.
        """
        self.assertEqual(celsius_to_fahrenheit(-101), "Invalid Temperature")

class TestValidateCreditCard(unittest.TestCase):
    """
    Class for testing the validate_credit_card function.
    """
    def test_valid_card_length_13(self):
        """
        Test a valid card number with 13 digits.
        """
        self.assertEqual(validate_credit_card("1234567890123"), "Valid Card")

    def test_valid_card_length_16(self):
        """
        Test a valid card number with 16 digits.
        """
        self.assertEqual(validate_credit_card("1234567890123456"), "Valid Card")

    def test_invalid_card_length_short(self):
        """
        Test an invalid card number that is too short.
        """
        self.assertEqual(validate_credit_card("1234567"), "Invalid Card")

    def test_invalid_card_length_long(self):
        """
        Test an invalid card number that is too long.
        """
        self.assertEqual(validate_credit_card("12345678901234567"), "Invalid Card")

    def test_invalid_card_non_numeric(self):
        """
        Test an invalid card number with non-numeric characters.
        """
        self.assertEqual(validate_credit_card("1234abcd9012"), "Invalid Card")

class TestValidateDate(unittest.TestCase):
    """
    Class for testing the validate_date function.
    """
    def test_valid_date(self):
        """
        Test a valid date.
        """
        self.assertEqual(validate_date(2020, 5, 15), "Valid Date")

    def test_invalid_year_low(self):
        """
        Test an invalid year that is too low.
        """
        self.assertEqual(validate_date(1899, 12, 31), "Invalid Date")

    def test_invalid_year_high(self):
        """
        Test an invalid year that is too high.
        """
        self.assertEqual(validate_date(2101, 1, 1), "Invalid Date")

    def test_invalid_month_low(self):
        """
        Test an invalid month that is too low.
        """
        self.assertEqual(validate_date(2020, 0, 15), "Invalid Date")

    def test_invalid_month_high(self):
        """
        Test an invalid month that is too high.
        """
        self.assertEqual(validate_date(2020, 13, 15), "Invalid Date")

    def test_invalid_day_low(self):
        """
        Test an invalid day that is too low.
        """
        self.assertEqual(validate_date(2020, 5, 0), "Invalid Date")

    def test_invalid_day_high(self):
        """
        Test an invalid day that is too high.
        """
        self.assertEqual(validate_date(2020, 5, 32), "Invalid Date")

class TestCheckFlightEligibility(unittest.TestCase):
    """
    Class for testing the check_flight_eligibility function.
    """
    def test_eligible_by_age(self):
        """
        Test eligibility based on age.
        """
        self.assertEqual(check_flight_eligibility(25, False), "Eligible to Book")

    def test_eligible_as_frequent_flyer(self):
        """
        Test eligibility as a frequent flyer.
        """
        self.assertEqual(check_flight_eligibility(17, True), "Eligible to Book")

    def test_not_eligible_by_age(self):
        """
        Test ineligibility based on age.
        """
        self.assertEqual(check_flight_eligibility(16, False), "Not Eligible to Book")

    def test_eligible_over_age_limit(self):
        """
        Test eligibility over the age limit.
        """
        self.assertEqual(check_flight_eligibility(66, False), "Not Eligible to Book")

class TestValidateURL(unittest.TestCase):
    """
    Class for testing the validate_url function.
    """
    def test_valid_http_url(self):
        """
        Test a valid HTTP URL.
        """
        self.assertEqual(validate_url("http://example.com"), "Valid URL")

    def test_valid_https_url(self):
        """
        Test a valid HTTPS URL.
        """
        self.assertEqual(validate_url("https://example.com"), "Valid URL")

    def test_invalid_url_no_protocol(self):
        """
        Test an invalid URL without a protocol.
        """
        self.assertEqual(validate_url("example.com"), "Invalid URL")

    def test_invalid_url_long(self):
        """
        Test an invalid URL that is too long.
        """
        self.assertEqual(validate_url("http://" + "a" * 250 + ".com"), "Invalid URL")

class TestCalculateQuantityDiscount(unittest.TestCase):
    """
    Class for testing the calculate_quantity_discount function.
    """
    def test_no_discount(self):
        """
        Test no discount for quantity 1-5.
        """
        self.assertEqual(calculate_quantity_discount(3), "No Discount")

    def test_5_percent_discount(self):
        """
        Test 5% discount for quantity 6-10.
        """
        self.assertEqual(calculate_quantity_discount(7), "5% Discount")

    def test_10_percent_discount(self):
        """
        Test 10% discount for quantity >10.
        """
        self.assertEqual(calculate_quantity_discount(11), "10% Discount")

class TestCheckFileSize(unittest.TestCase):
    """
    Class for testing the check_file_size function.
    """
    def test_valid_file_size(self):
        """
        Test a valid file size.
        """
        self.assertEqual(check_file_size(512000), "Valid File Size")

    def test_invalid_file_size_large(self):
        """
        Test an invalid file size that is too large.
        """
        self.assertEqual(check_file_size(1048577), "Invalid File Size")

class TestCheckLoanEligibility(unittest.TestCase):
    """
    Class for testing the check_loan_eligibility function.
    """
    def test_not_eligible_low_income(self):
        """
        Test ineligibility due to low income.
        """
        self.assertEqual(check_loan_eligibility(25000, 720), "Not Eligible")

    def test_secured_loan(self):
        """
        Test eligibility for a secured loan.
        """
        self.assertEqual(check_loan_eligibility(40000, 700), "Secured Loan")

    def test_standard_loan_high_income_low_score(self):
        """
        Test eligibility for a standard loan.
        """
        self.assertEqual(check_loan_eligibility(70000, 720), "Standard Loan")

    def test_premium_loan(self):
        """
        Test eligibility for a premium loan.
        """
        self.assertEqual(check_loan_eligibility(80000, 760), "Premium Loan")

class TestCheckLoanEligibility(unittest.TestCase):
    """
    Class for testing the check_loan_eligibility function.
    """
    def test_not_eligible_low_income(self):
        """
        test not eligible low income
        """
        self.assertEqual(check_loan_eligibility(25000, 720), "Not Eligible")

    def test_secured_loan(self):
        """
        test secured loan
        """
        self.assertEqual(check_loan_eligibility(40000, 700), "Secured Loan")

    def test_standard_loan_high_income_low_score(self):
        """
        test standard loan
        """
        self.assertEqual(check_loan_eligibility(70000, 720), "Standard Loan")

    def test_premium_loan(self):
        """
        test premium loan
        """
        self.assertEqual(check_loan_eligibility(80000, 760), "Premium Loan")

class TestCalculateShippingCost(unittest.TestCase):
    """
    Class for testing the calculate_shipping_cost function.
    """
    def test_small_light_package(self):
        """
        Test a small, light package.
        """
        self.assertEqual(calculate_shipping_cost(0.5, 5, 5, 5), 5)

    def test_medium_weight_package(self):
        """
        Test a medium weight package.
        """
        self.assertEqual(calculate_shipping_cost(3, 20, 20, 20), 10)

    def test_large_heavy_package(self):
        """
        Test a large, heavy package.
        """
        self.assertEqual(calculate_shipping_cost(10, 40, 40, 40), 20)

class TestGradeQuiz(unittest.TestCase):
    """
    Class for testing the grade_quiz function.
    """
    def test_pass(self):
        """
        Test a passing grade.
        """
        self.assertEqual(grade_quiz(8, 2), "Pass")

    def test_conditional_pass(self):
        """
        Test a conditional pass grade.
        """
        self.assertEqual(grade_quiz(5, 3), "Conditional Pass")

    def test_fail(self):
        """
        Test a failing grade.
        """
        self.assertEqual(grade_quiz(4, 5), "Fail")

class TestAuthenticateUser(unittest.TestCase):
    """
    Class for testing the authenticate_user function.
    """
    def test_admin_login(self):
        """
        Test an admin login.
        """
        self.assertEqual(authenticate_user("admin", "admin123"), "Admin")

    def test_user_login(self):
        """
        Test a user login.
        """
        self.assertEqual(authenticate_user("user1234", "password1234"), "User")

    def test_invalid_login(self):
        """
        Test an invalid login.
        """
        self.assertEqual(authenticate_user("usr", "pwd"), "Invalid")

class TestGetWeatherAdvisory(unittest.TestCase):
    """
    Class for testing the get_weather_advisory function.
    """
    def test_high_temp_humidity(self):
        """
        Test high temperature and humidity.
        """
        self.assertEqual(get_weather_advisory(35, 75), "High Temperature and Humidity. Stay Hydrated.")

    def test_low_temperature(self):
        """
        Test low temperature.
        """
        self.assertEqual(get_weather_advisory(-5, 50), "Low Temperature. Bundle Up!")

    def test_no_specific_advisory(self):
        """
        Test no specific advisory.
        """
        self.assertEqual(get_weather_advisory(20, 50), "No Specific Advisory")

class TestVendingMachine(unittest.TestCase):
    """
    Class for testing the VendingMachine class.
    """
    def setUp(self):
        """
        Set up the VendingMachine instance for testing.
        """
        self.vm = VendingMachine()

    def test_insert_coin(self):
        """
        Test inserting a coin.
        """
        self.assertEqual(self.vm.insert_coin(), "Coin Inserted. Select your drink.")

    def test_select_drink(self):
        """
        Test selecting a drink.
        """
        self.vm.insert_coin()
        self.assertEqual(self.vm.select_drink(), "Drink Dispensed. Thank you!")

    def test_invalid_operation(self):
        """
        Test an invalid operation.
        """
        self.assertEqual(self.vm.select_drink(), "Invalid operation in current state.")

class TestTrafficLight(unittest.TestCase):
    """
    Class for testing the TrafficLight class.
    """

    def test_change_state(self):
        """
        Test change_state when the light is red.
        """
        light = TrafficLight()
        self.assertEqual(light.state, "Red")
        light.change_state()
        self.assertEqual(light.state, "Green")

    def test_change_state_when_green(self):
        """
        Test change_state when the light is green.
        """
        light = TrafficLight()
        light.state = "Green"
        light.change_state()
        self.assertEqual(light.state, "Yellow")

    def test_change_state_when_yellow(self):
        """
        Test change_state when the light is yellow.
        """
        light = TrafficLight()
        light.state = "Yellow"
        light.change_state()
        self.assertEqual(light.state, "Red")

    def test_change_state_when_invalid(self):
        """
        Test change_state when the light is in an invalid state.
        """
        light = TrafficLight()
        light.state = "Invalid"
        light.change_state()
        self.assertEqual(light.state, "Invalid")

class TestUserAuthentication(unittest.TestCase):
    """
    Class for testing the UserAuthentication class.
    """
    def setUp(self):
        """
        Set up the UserAuthentication instance for testing.
        """
        self.auth = UserAuthentication()

    def test_login(self):
        """
        Test logging in.
        """
        self.assertEqual(self.auth.login(), "Login successful")

    def test_logout(self):
        """
        Test logging out.
        """
        self.auth.login()
        self.assertEqual(self.auth.logout(), "Logout successful")

    def test_invalid_login(self):
        """
        Test an invalid login.
        """
        self.auth.login()  # Change state to Logged In
        self.assertEqual(self.auth.login(), "Invalid operation in current state")

    def test_invalid_logout(self):
        """
        Test an invalid logout.
        """
        self.assertEqual(self.auth.logout(), "Invalid operation in current state")

class TestDocumentEditingSystem(unittest.TestCase):
    """
    Class for testing the DocumentEditingSystem class.
    """
    def setUp(self):
        """
        Set up the DocumentEditingSystem instance for testing.
        """
        self.doc_system = DocumentEditingSystem()

    def test_save_document(self):
        """
        Test saving a document.
        """
        self.assertEqual(self.doc_system.save_document(), "Document saved successfully")

    def test_edit_document(self):
        """
        Test editing a document.
        """
        self.doc_system.save_document()  # Change state to Saved
        self.assertEqual(self.doc_system.edit_document(), "Editing resumed")

    def test_invalid_save(self):
        """
        Test an invalid save operation.
        """
        self.doc_system.save_document()  # Change state to Saved
        self.assertEqual(self.doc_system.save_document(), "Invalid operation in current state")

    def test_invalid_edit(self):
        """
        Test an invalid edit operation.
        """
        self.assertEqual(self.doc_system.edit_document(), "Invalid operation in current state")

class TestElevatorSystem(unittest.TestCase):
    """
    Class for testing the ElevatorSystem class.
    """
    def setUp(self):
        """
        Set up the ElevatorSystem instance for testing.
        """
        self.elevator = ElevatorSystem()

    def test_move_up(self):
        """
        Test moving the elevator up.
        """
        self.assertEqual(self.elevator.move_up(), "Elevator moving up")

    def test_move_down(self):
        """
        Test moving the elevator down.
        """
        self.assertEqual(self.elevator.move_down(), "Elevator moving down")

    def test_stop_from_moving_up(self):
        """
        Test stopping the elevator when moving up.
        """
        self.elevator.move_up()  # Change state to Moving Up
        self.assertEqual(self.elevator.stop(), "Elevator stopped")

    def test_stop_from_moving_down(self):
        """
        Test stopping the elevator when moving down.
        """
        self.elevator.move_down()  # Change state to Moving Down
        self.assertEqual(self.elevator.stop(), "Elevator stopped")

    def test_invalid_operation_when_moving(self):
        """
        Test an invalid operation when the elevator is moving.
        """
        self.elevator.move_up()  # Change state to Moving Up
        self.assertEqual(self.elevator.move_up(), "Invalid operation in current state")
        self.assertEqual(self.elevator.move_down(), "Invalid operation in current state")

class TestBankingSystem(unittest.TestCase):
    """
    Class for testing the BankingSystem class.
    """
    def setUp(self):
        """
        Set up the BankingSystem instance for testing.
        """
        self.banking_system = BankingSystem()

    def test_authenticate_success(self):
        """
        Test a successful authentication.
        """
        self.assertTrue(self.banking_system.authenticate("user123", "pass123"))

    def test_authenticate_failure(self):
        """
        Test a failed authentication.
        """
        self.assertFalse(self.banking_system.authenticate("user123", "wrongpass"))

    def test_authenticate_already_logged_in(self):
        """
        Test an authentication when already logged in.
        """
        self.banking_system.authenticate("user123", "pass123")
        self.assertFalse(self.banking_system.authenticate("user123", "pass123"))

    def test_transfer_money_not_authenticated(self):
        """
        Test transferring money when not authenticated.
        """
        self.assertFalse(self.banking_system.transfer_money("user123", "receiver", 100, "regular"))

    def test_transfer_money_invalid_transaction_type(self):
        """
        Test transferring money with an invalid transaction type.
        """
        self.banking_system.authenticate("user123", "pass123")
        self.assertFalse(self.banking_system.transfer_money("user123", "receiver", 100, "invalid_type"))

    def test_transfer_money_insufficient_funds(self):
        """
        Test transferring money with insufficient funds.
        """
        self.banking_system.authenticate("user123", "pass123")
        self.assertFalse(self.banking_system.transfer_money("user123", "receiver", 2000, "regular"))

    def test_transfer_money_success(self):
        """
        Test a successful money transfer.
        """
        self.banking_system.authenticate("user123", "pass123")
        self.assertTrue(self.banking_system.transfer_money("user123", "receiver", 100, "regular"))

class TestProduct(TestCase):
    """
    Class for testing the Product class.
    """
    def setUp(self):
        """
        Set up the Product instance for testing.
        """
        self.product = Product("Test Product", 100)

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_view_product(self, mock_stdout):
        """
        Test the view_product method.
        """
        self.product.view_product()
        self.assertEqual(mock_stdout.getvalue().strip(), "The product Test Product has a price of 100")

if __name__ == "__main__":
    unittest.main()
