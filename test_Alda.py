# -*- coding: utf-8 -*-

"""
 White-box unit testing examples.
"""

import unittest
import functions


# #2
# print("Test check_number_status")

# def test_validate_password_lenght():
#     assert functions.validate_password('Aa@12345') == True
#     assert functions.validate_password('Aa@1234') == False

# def test_validate_password_withoutUppercase():
#     assert functions.validate_password('a@123456') == False

# def test_validate_password_withoutLowercase():
#     assert functions.validate_password('A@123456') == False

# def test_validate_password_withoutDigit():
#     assert functions.validate_password('Aa@aaaaa') == False

# def test_validate_password_withoutSpecialCharacter():
#     assert functions.validate_password('Aa123456') == False


# #4
# print("Test calculate_order_total")

# def test_calculate_order_total_1to5():
#     assert functions.calculate_order_total([{'quantity': 1, 'price': 100}]) == 100
#     assert functions.calculate_order_total([{'quantity': 5, 'price': 100}]) == 500

# def test_calculate_order_total_6to10():
#     assert functions.calculate_order_total([{'quantity': 6, 'price': 100}]) == 570
#     assert functions.calculate_order_total([{'quantity': 10, 'price': 100}]) == 950

# def test_calculate_order_total_gt11():
#     assert functions.calculate_order_total([{'quantity': 11, 'price': 100}]) == 990



# #6
# print("Test validate_login")

# def test_validate_login_usernameLength():
#     assert functions.validate_login('12345', '12345678') == 'Login Successful'
#     assert functions.validate_login('1234', '12345678') == 'Login Failed'
#     assert functions.validate_login('12345678912345678912', '12345678') == 'Login Successful'
#     assert functions.validate_login('123456789123456789123', '12345678') == 'Login Failed'

# def test_validate_login_passwordLength():
#     assert functions.validate_login('Aldai', '12345678') == 'Login Successful'
#     assert functions.validate_login('Aldai', '1234567') == 'Login Failed'


class TestWhiteBox(unittest.TestCase):
    """
    White-box unittest class.
    """
    #24
    def test_login_successul(self):
        """
        Checks login
        """
        prueba = functions.UserAuthentication()
        self.assertEquals(prueba.login(), "Login successful")

    def test_login_invalid(self):
        """
        Checks login
        """
        prueba = functions.UserAuthentication()
        self.assertEquals(prueba.login(), "Login successful")
        self.assertEquals(prueba.login(), "Invalid operation in current state")


    def test_logout_successful(self):
        """
        Checks logout
        """
        prueba = functions.UserAuthentication()
        self.assertEquals(prueba.login(), "Login successful")
        self.assertEquals(prueba.logout(), "Logout successful")


    def test_logout_invalid(self):
        """
        Checks logout
        """
        prueba = functions.UserAuthentication()
        self.assertEquals(prueba.logout(), "Invalid operation in current state")


    #25
    def test_save_document_successful(self):
        """
        Checks save document
        """
        prueba = functions.DocumentEditingSystem()
        self.assertAlmostEquals(prueba.save_document(), "Document saved successfully")

    def test_save_document_invalid(self):
        """
        Checks save document
        """
        prueba = functions.DocumentEditingSystem()
        self.assertAlmostEquals(prueba.save_document(), "Document saved successfully")
        self.assertAlmostEquals(prueba.save_document(), "Invalid operation in current state")

    def test_edit_document_successful(self):
        """
        Checks save document
        """
        prueba = functions.DocumentEditingSystem()
        self.assertAlmostEquals(prueba.save_document(), "Document saved successfully")
        self.assertAlmostEquals(prueba.edit_document(), "Editing resumed")

    def test_edit_document_invalid(self):
        """
        Checks save document
        """
        prueba = functions.DocumentEditingSystem()
        self.assertAlmostEquals(prueba.edit_document(), "Invalid operation in current state")

if __name__ == "__main__":
    unittest.main()
