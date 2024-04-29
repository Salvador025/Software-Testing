import subprocess
import time
import unittest
from unittest.mock import MagicMock, mock_open, patch

from mockup_homework import (
    execute_command,
    perform_action_based_on_time,
    read_data_from_file,
)


class TestFileOperations(unittest.TestCase):
    """
    Test the file reading functionality.
    """

    @patch("builtins.open", new_callable=mock_open, read_data="data")
    def test_read_data_from_file(self, mock_file):
        """
        Test reading data from file.
        """
        # Call the function under test
        result = read_data_from_file("dummy_filename.txt")

        # Assert that the function reads the data correctly
        self.assertEqual(result, "data")

        # Assert that open was called correctly
        mock_file.assert_called_once_with("dummy_filename.txt", "r")

    @patch("builtins.open", new_callable=mock_open, read_data="data")
    def test_read_data_from_file_not_found_error(self, mock_file):
        """
        Test file not found error.
        """
        mock_file.side_effect = FileNotFoundError("File not found")

        # Assert that FileNotFoundError is raised
        with self.assertRaises(FileNotFoundError):
            read_data_from_file("dummy_filename.txt")


class TestCommandExecution(unittest.TestCase):
    """
    Test command execution functionality.
    """

    @patch("subprocess.run")
    def test_execute_command_success(self, mock_run):
        """
        Test successful command execution.
        """
        mock_run.return_value = MagicMock(stdout="Execution success", returncode=0)

        # Call the function under test
        result = execute_command(["echo", "hello"])

        # Assert that the function returns the expected result
        self.assertEqual(result, "Execution success")

    @patch("subprocess.run")
    def test_execute_command_failure(self, mock_run):
        """
        Test command execution failure.
        """
        mock_run.side_effect = subprocess.CalledProcessError(
            returncode=1, cmd=["exit", "1"]
        )

        # Assert that CalledProcessError is raised
        with self.assertRaises(subprocess.CalledProcessError):
            execute_command(["exit", "1"])


class TestTimeBasedAction(unittest.TestCase):
    """
    Test time-based action functionality.
    """

    @patch("time.time", return_value=5)
    def test_perform_action_based_on_time_action_a(self, mock_time):
        """
        Test performing Action A based on time.
        """
        result = perform_action_based_on_time()
        self.assertEqual(result, "Action A")

    @patch("time.time", return_value=11)
    def test_perform_action_based_on_time_action_b(self, mock_time):
        """
        Test performing Action B based on time.
        """
        result = perform_action_based_on_time()
        self.assertEqual(result, "Action B")


if __name__ == "__main__":
    unittest.main()
