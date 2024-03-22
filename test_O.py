"""
Unit test functions 26-27
"""

from functions import ElevatorSystem
from functions import BankAccount, BankingSystem

print("Elevator Sytmen class testing")

Elevator = ElevatorSystem()

def test_idle_state_elevator():
    assert Elevator.state == "Idle"

def test_move_up_elevator():
    assert Elevator.move_up() == "Elevator moving up"
    assert Elevator.move_up() == "Invalid operation in current state"

def test_stop_elevator():
    assert Elevator.stop() == "Elevator stopped"
    assert Elevator.stop() == "Invalid operation in current state"

def test_move_down_elevator():
    assert Elevator.move_down() == "Elevator moving down"
    assert Elevator.move_down() == "Invalid operation in current state"


print("Bank Account and Bank Testing class testing")

def test_view_account():
    account =  BankAccount(112233, 10000)
    assert account.view_account() == True

def test_auth_system():
    system = BankingSystem()
    assert system.authenticate("user123", "pass123") == True
    assert system.authenticate("user1", "pass123") == False

def test_transfer_money_system():
    system = BankingSystem()
    assert system.transfer_money("user123", "user1", 500, "regular") == False
    system.authenticate("user123", "pass123")
    assert system.transfer_money("user123", "user1", 500, "regular") == True
    assert system.transfer_money("user123", "user1", 500, "express") == True
    assert system.transfer_money("user123", "user1", 500, "scheduled") == True
    assert system.transfer_money("user123", "user1", 500, "fast") == False
    assert system.transfer_money("user123", "user1", 1100, "regular") == False
