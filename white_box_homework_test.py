"""
 White-box unit testing examples.
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
        self.assertEqual(validate_login("user123", "password123"), "Login Successful")

    def test_invalid_username_short(self):
        self.assertEqual(validate_login("usr", "password123"), "Login Failed")

    def test_invalid_username_long(self):
        self.assertEqual(validate_login("a" * 21, "password123"), "Login Failed")

    def test_invalid_password_short(self):
        self.assertEqual(validate_login("user123", "pass"), "Login Failed")

    def test_invalid_password_long(self):
        self.assertEqual(validate_login("user123", "p" * 16), "Login Failed")

class TestVerifyAge(unittest.TestCase):
    """
    Tests for the verify_age function.
    """

    def test_age_eligible(self):
        self.assertEqual(verify_age(25), "Eligible")

    def test_age_young(self):
        self.assertEqual(verify_age(17), "Not Eligible")

    def test_age_old(self):
        self.assertEqual(verify_age(66), "Not Eligible")

class TestCategorizeProduct(unittest.TestCase):
    def test_category_a(self):
        self.assertEqual(categorize_product(25), "Category A")

    def test_category_b(self):
        self.assertEqual(categorize_product(75), "Category B")

    def test_category_c(self):
        self.assertEqual(categorize_product(150), "Category C")

    def test_category_d(self):
        self.assertEqual(categorize_product(250), "Category D")

class TestValidateEmail(unittest.TestCase):
    def test_valid_email(self):
        self.assertEqual(validate_email("test@example.com"), "Valid Email")

    def test_invalid_email_no_at(self):
        self.assertEqual(validate_email("testexample.com"), "Invalid Email")

    def test_invalid_email_no_dot(self):
        self.assertEqual(validate_email("test@examplecom"), "Invalid Email")

    def test_invalid_email_too_short(self):
        self.assertEqual(validate_email("t@e.c"), "Valid Email")

    def test_invalid_email_too_long(self):
        self.assertEqual(validate_email("t" * 51 + "@example.com"), "Invalid Email")

class TestCelsiusToFahrenheit(unittest.TestCase):
    def test_valid_conversion(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(25), 77)

    def test_invalid_temperature(self):
        self.assertEqual(celsius_to_fahrenheit(-101), "Invalid Temperature")

class TestValidateCreditCard(unittest.TestCase):
    def test_valid_card_length_13(self):
        self.assertEqual(validate_credit_card("1234567890123"), "Valid Card")

    def test_valid_card_length_16(self):
        self.assertEqual(validate_credit_card("1234567890123456"), "Valid Card")

    def test_invalid_card_length_short(self):
        self.assertEqual(validate_credit_card("1234567"), "Invalid Card")

    def test_invalid_card_length_long(self):
        self.assertEqual(validate_credit_card("12345678901234567"), "Invalid Card")

    def test_invalid_card_non_numeric(self):
        self.assertEqual(validate_credit_card("1234abcd9012"), "Invalid Card")

class TestValidateDate(unittest.TestCase):
    def test_valid_date(self):
        self.assertEqual(validate_date(2020, 5, 15), "Valid Date")

    def test_invalid_year_low(self):
        self.assertEqual(validate_date(1899, 12, 31), "Invalid Date")

    def test_invalid_year_high(self):
        self.assertEqual(validate_date(2101, 1, 1), "Invalid Date")

    def test_invalid_month_low(self):
        self.assertEqual(validate_date(2020, 0, 15), "Invalid Date")

    def test_invalid_month_high(self):
        self.assertEqual(validate_date(2020, 13, 15), "Invalid Date")

    def test_invalid_day_low(self):
        self.assertEqual(validate_date(2020, 5, 0), "Invalid Date")

    def test_invalid_day_high(self):
        self.assertEqual(validate_date(2020, 5, 32), "Invalid Date")

class TestCheckFlightEligibility(unittest.TestCase):
    def test_eligible_by_age(self):
        self.assertEqual(check_flight_eligibility(25, False), "Eligible to Book")

    def test_eligible_as_frequent_flyer(self):
        self.assertEqual(check_flight_eligibility(17, True), "Eligible to Book")

    def test_not_eligible_by_age(self):
        self.assertEqual(check_flight_eligibility(16, False), "Not Eligible to Book")

    def test_eligible_over_age_limit(self):
        self.assertEqual(check_flight_eligibility(66, False), "Not Eligible to Book")

class TestValidateURL(unittest.TestCase):
    def test_valid_http_url(self):
        self.assertEqual(validate_url("http://example.com"), "Valid URL")

    def test_valid_https_url(self):
        self.assertEqual(validate_url("https://example.com"), "Valid URL")

    def test_invalid_url_no_protocol(self):
        self.assertEqual(validate_url("example.com"), "Invalid URL")

    def test_invalid_url_long(self):
        self.assertEqual(validate_url("http://" + "a" * 250 + ".com"), "Invalid URL")

class TestCalculateQuantityDiscount(unittest.TestCase):
    def test_no_discount(self):
        self.assertEqual(calculate_quantity_discount(3), "No Discount")

    def test_5_percent_discount(self):
        self.assertEqual(calculate_quantity_discount(7), "5% Discount")

    def test_10_percent_discount(self):
        self.assertEqual(calculate_quantity_discount(11), "10% Discount")

class TestCheckFileSize(unittest.TestCase):
    def test_valid_file_size(self):
        self.assertEqual(check_file_size(512000), "Valid File Size")

    def test_invalid_file_size_large(self):
        self.assertEqual(check_file_size(1048577), "Invalid File Size")

class TestCheckLoanEligibility(unittest.TestCase):
    def test_not_eligible_low_income(self):
        self.assertEqual(check_loan_eligibility(25000, 720), "Not Eligible")

    def test_secured_loan(self):
        self.assertEqual(check_loan_eligibility(40000, 700), "Secured Loan")

    def test_standard_loan_high_income_low_score(self):
        self.assertEqual(check_loan_eligibility(70000, 720), "Standard Loan")

    def test_premium_loan(self):
        self.assertEqual(check_loan_eligibility(80000, 760), "Premium Loan")

class TestCheckLoanEligibility(unittest.TestCase):
    def test_not_eligible_low_income(self):
        self.assertEqual(check_loan_eligibility(25000, 720), "Not Eligible")

    def test_secured_loan(self):
        self.assertEqual(check_loan_eligibility(40000, 700), "Secured Loan")

    def test_standard_loan_high_income_low_score(self):
        self.assertEqual(check_loan_eligibility(70000, 720), "Standard Loan")

    def test_premium_loan(self):
        self.assertEqual(check_loan_eligibility(80000, 760), "Premium Loan")

class TestCalculateShippingCost(unittest.TestCase):
    def test_small_light_package(self):
        self.assertEqual(calculate_shipping_cost(0.5, 5, 5, 5), 5)

    def test_medium_weight_package(self):
        self.assertEqual(calculate_shipping_cost(3, 20, 20, 20), 10)

    def test_large_heavy_package(self):
        self.assertEqual(calculate_shipping_cost(10, 40, 40, 40), 20)

class TestGradeQuiz(unittest.TestCase):
    def test_pass(self):
        self.assertEqual(grade_quiz(8, 2), "Pass")

    def test_conditional_pass(self):
        self.assertEqual(grade_quiz(5, 3), "Conditional Pass")

    def test_fail(self):
        self.assertEqual(grade_quiz(4, 5), "Fail")

class TestAuthenticateUser(unittest.TestCase):
    def test_admin_login(self):
        self.assertEqual(authenticate_user("admin", "admin123"), "Admin")

    def test_user_login(self):
        self.assertEqual(authenticate_user("user1234", "password1234"), "User")

    def test_invalid_login(self):
        self.assertEqual(authenticate_user("usr", "pwd"), "Invalid")

class TestGetWeatherAdvisory(unittest.TestCase):
    def test_high_temp_humidity(self):
        self.assertEqual(get_weather_advisory(35, 75), "High Temperature and Humidity. Stay Hydrated.")

    def test_low_temperature(self):
        self.assertEqual(get_weather_advisory(-5, 50), "Low Temperature. Bundle Up!")

    def test_no_specific_advisory(self):
        self.assertEqual(get_weather_advisory(20, 50), "No Specific Advisory")

class TestVendingMachine(unittest.TestCase):
    def setUp(self):
        self.vm = VendingMachine()

    def test_insert_coin(self):
        self.assertEqual(self.vm.insert_coin(), "Coin Inserted. Select your drink.")

    def test_select_drink(self):
        self.vm.insert_coin()
        self.assertEqual(self.vm.select_drink(), "Drink Dispensed. Thank you!")

    def test_invalid_operation(self):
        self.assertEqual(self.vm.select_drink(), "Invalid operation in current state.")

class TestTrafficLight(unittest.TestCase):

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
    def setUp(self):
        self.auth = UserAuthentication()

    def test_login(self):
        self.assertEqual(self.auth.login(), "Login successful")

    def test_logout(self):
        self.auth.login()
        self.assertEqual(self.auth.logout(), "Logout successful")

    def test_invalid_login(self):
        self.auth.login()  # Change state to Logged In
        self.assertEqual(self.auth.login(), "Invalid operation in current state")

    def test_invalid_logout(self):
        self.assertEqual(self.auth.logout(), "Invalid operation in current state")

class TestDocumentEditingSystem(unittest.TestCase):
    def setUp(self):
        self.doc_system = DocumentEditingSystem()

    def test_save_document(self):
        self.assertEqual(self.doc_system.save_document(), "Document saved successfully")

    def test_edit_document(self):
        self.doc_system.save_document()  # Change state to Saved
        self.assertEqual(self.doc_system.edit_document(), "Editing resumed")

    def test_invalid_save(self):
        self.doc_system.save_document()  # Change state to Saved
        self.assertEqual(self.doc_system.save_document(), "Invalid operation in current state")

    def test_invalid_edit(self):
        self.assertEqual(self.doc_system.edit_document(), "Invalid operation in current state")

class TestElevatorSystem(unittest.TestCase):
    def setUp(self):
        self.elevator = ElevatorSystem()

    def test_move_up(self):
        self.assertEqual(self.elevator.move_up(), "Elevator moving up")

    def test_move_down(self):
        self.assertEqual(self.elevator.move_down(), "Elevator moving down")

    def test_stop_from_moving_up(self):
        self.elevator.move_up()  # Change state to Moving Up
        self.assertEqual(self.elevator.stop(), "Elevator stopped")

    def test_stop_from_moving_down(self):
        self.elevator.move_down()  # Change state to Moving Down
        self.assertEqual(self.elevator.stop(), "Elevator stopped")

    def test_invalid_operation_when_moving(self):
        self.elevator.move_up()  # Change state to Moving Up
        self.assertEqual(self.elevator.move_up(), "Invalid operation in current state")
        self.assertEqual(self.elevator.move_down(), "Invalid operation in current state")

class TestBankingSystem(unittest.TestCase):
    def setUp(self):
        self.banking_system = BankingSystem()

    def test_authenticate_success(self):
        self.assertTrue(self.banking_system.authenticate("user123", "pass123"))

    def test_authenticate_failure(self):
        self.assertFalse(self.banking_system.authenticate("user123", "wrongpass"))

    def test_authenticate_already_logged_in(self):
        self.banking_system.authenticate("user123", "pass123")
        self.assertFalse(self.banking_system.authenticate("user123", "pass123"))

    def test_transfer_money_not_authenticated(self):
        self.assertFalse(self.banking_system.transfer_money("user123", "receiver", 100, "regular"))

    def test_transfer_money_invalid_transaction_type(self):
        self.banking_system.authenticate("user123", "pass123")
        self.assertFalse(self.banking_system.transfer_money("user123", "receiver", 100, "invalid_type"))

    def test_transfer_money_insufficient_funds(self):
        self.banking_system.authenticate("user123", "pass123")
        self.assertFalse(self.banking_system.transfer_money("user123", "receiver", 2000, "regular"))

    def test_transfer_money_success(self):
        self.banking_system.authenticate("user123", "pass123")
        self.assertTrue(self.banking_system.transfer_money("user123", "receiver", 100, "regular"))

class TestProduct(TestCase):
    def setUp(self):
        self.product = Product("Test Product", 100)

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_view_product(self, mock_stdout):
        self.product.view_product()
        self.assertEqual(mock_stdout.getvalue().strip(), "The product Test Product has a price of 100")

if __name__ == "__main__":
    unittest.main()
