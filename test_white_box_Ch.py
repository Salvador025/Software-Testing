"""Test cases for functions #22 and #23."""
import unittest
from functions import VendingMachine, TrafficLight # Importa la clase VendingMachine

class TestVendingMachine(unittest.TestCase):

    def test_insert_coin_when_ready(self):
        """
        Test insert_coin when the machine is ready.
        """
        machine = VendingMachine()
        response = machine.insert_coin()
        self.assertEqual(response, "Coin Inserted. Select your drink.")
        self.assertEqual(machine.state, "Dispensing")


    def test_insert_coin_when_not_ready(self):
        """
        Test insert_coin when the machine is not ready (i.e., dispensing).
        """
        machine = VendingMachine()
        machine.state = "Dispensing"  # Set the machine to a non-ready state
        response = machine.insert_coin()
        self.assertEqual(response, "Invalid operation in current state.")
        self.assertEqual(machine.state, "Dispensing")

    def test_select_drink_when_dispensing(self):
        """
        Test select_drink when the machine is dispensing.
        """
        machine = VendingMachine()
        machine.state = "Dispensing"
        response = machine.select_drink()
        self.assertEqual(response, "Drink Dispensed. Thank you!")
        self.assertEqual(machine.state, "Ready")

    def test_select_drink_when_not_dispensing(self):
        """
        Test select_drink when the machine is not dispensing (i.e., ready).
        """
        machine = VendingMachine()
        # Here we assume the machine state is already "Ready"
        response = machine.select_drink()
        self.assertEqual(response, "Invalid operation in current state.")
        self.assertEqual(machine.state, "Ready")

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


if __name__ == '__main__':
    unittest.main()
