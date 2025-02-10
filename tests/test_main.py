import unittest
from unittest.mock import patch, MagicMock
from main import main, basic_calculator, advanced_calculator

class TestMain(unittest.TestCase):
    @patch('builtins.input', side_effect=['3'])
    @patch('builtins.print')
    def test_main_exit(self, mock_print, mock_input):
        main()
        mock_print.assert_any_call('Comprehensive Calculator')

    @patch('builtins.input', side_effect=['1', '2', '+', '3'])
    @patch('builtins.print')
    def test_basic_calculator_add(self, mock_print, mock_input):
        basic_calculator()
        mock_print.assert_any_call('Result: 5.0')

    @patch('builtins.input', side_effect=['2', '2', '/', '0'])
    @patch('builtins.print')
    def test_basic_calculator_divide_by_zero(self, mock_print, mock_input):
        basic_calculator()
        mock_print.assert_any_call('Error: Cannot divide by zero')

    @patch('builtins.input', side_effect=['1', '2', '3'])
    @patch('builtins.print')
    def test_advanced_calculator_power(self, mock_print, mock_input):
        advanced_calculator()
        mock_print.assert_any_call('Result: 8.0')

    @patch('builtins.input', side_effect=['2', '-4'])
    @patch('builtins.print')
    def test_advanced_calculator_square_root_negative(self, mock_print, mock_input):
        advanced_calculator()
        mock_print.assert_any_call('Error: Cannot calculate square root of negative number')

if __name__ == '__main__':
    unittest.main()