"""
This module contains unit tests for the functions defined in mockup_homework module.
"""

import subprocess
import unittest
from unittest.mock import MagicMock, mock_open, patch

from mockup_homework import (
    execute_command,
    perform_action_based_on_time,
    read_data_from_file,
)


class TestFileOperations(unittest.TestCase):
    """Test the file reading functionality."""

    @patch("builtins.open", new_callable=mock_open, read_data="data")
    def test_read_data_from_file(self, mock_file):
        """Test reading data from a file."""
        result = read_data_from_file("dummy_filename.txt")
        self.assertEqual(result, "data")
        mock_file.assert_called_once_with("dummy_filename.txt", "r", encoding="utf-8")

    @patch("builtins.open", new_callable=mock_open, read_data="data")
    def test_read_data_from_file_not_found_error(self, mock_file):
        """Test file not found error scenario."""
        mock_file.side_effect = FileNotFoundError("File not found")
        with self.assertRaises(FileNotFoundError):
            read_data_from_file("dummy_filename.txt")


class TestCommandExecution(unittest.TestCase):
    """Test command execution functionality."""

    @patch("subprocess.run")
    def test_execute_command_success(self, mock_run):
        """Test successful command execution."""
        mock_run.return_value = MagicMock(stdout="Execution success", returncode=0)
        result = execute_command(["echo", "hello"])
        self.assertEqual(result, "Execution success")

    @patch("subprocess.run")
    def test_execute_command_failure(self, mock_run):
        """Test command execution failure."""
        mock_run.side_effect = subprocess.CalledProcessError(
            returncode=1, cmd=["exit", "1"]
        )
        with self.assertRaises(subprocess.CalledProcessError):
            execute_command(["exit", "1"])


class TestTimeBasedAction(unittest.TestCase):
    """Test time-based action functionality."""

    @patch("time.time", return_value=5)
    def test_perform_action_based_on_time_action_a(self, result):
        """Test that 'Action A' is performed when current time is less than 10."""
        result = perform_action_based_on_time()
        self.assertEqual(result, "Action A")

    @patch("time.time", return_value=11)
    def test_perform_action_based_on_time_action_b(self, result):
        """Test that 'Action B' is performed when current time is 10 or more."""
        result = perform_action_based_on_time()
        self.assertEqual(result, "Action B")


if __name__ == "__main__":
    unittest.main()
