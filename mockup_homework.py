"""This module contains functions for reading data from a file,
executing a system command, and performing an action based on the
current system time.
"""

import subprocess
import time


def read_data_from_file(filename):
    """Read data from a file and return it.

    Args:
        filename (str): The path to the file to be read.

    Returns:
        str: The content of the file.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def execute_command(command):
    """Execute a system command and return its output.

    Args:
        command (list): The command to execute as a list of strings.

    Returns:
        str: The stdout from the command execution.

    Raises:
        subprocess.CalledProcessError: If the command returns a non-zero exit status.
    """
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return result.stdout


def perform_action_based_on_time():
    """Perform an action based on the current time.

    Returns:
        str: 'Action A' if the current time is less than 10,
             'Action B' otherwise.
    """
    if time.time() < 10:
        return "Action A"
    return "Action B"
