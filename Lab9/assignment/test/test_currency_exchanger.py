# Lab9 - Test double
# Integration testing using Mock - Crate Mock object to mimic the behavior of external service
# นายชนินทร์ ธัญสิริพัฒนธาดา 653380125-2 sec.1

from unittest.mock import patch
import sys
sys.path.insert(0,"/workspaces/Lab9_-TestDouble_653380125-2/Lab9/assignment/")
from source.currency_exchanger import CurrencyExchanger
from utils import get_mock_currency_exchange_api_response
import unittest


class TestCurrencyExchange(unittest.TestCase):
    def setUp(self):
        self.currencyExchanger = CurrencyExchanger()
        self.mock_api_response = get_mock_currency_exchange_api_response()
        self.currencyExchanger.target_currency = 'KRW'

    # Mock the 'request' package from source.country
    @patch("source.currency_exchanger.requests")
    def test_get_currency_rate(self, mock_request):
        # Assign mock's return value
        self.currencyExchanger.target_currency = 'KRW'
        mock_request.get.return_value = self.mock_api_response
        # Act - execute class under test
        self.currencyExchanger.get_currency_rate()
        # Check whether the mocked method is called
        mock_request.get.assert_called_once()
        # Check whether the mocked method is called with the right parameter
        mock_request.get.assert_called_with("https://coc-kku-bank.com/foreign-exchange", params={'from': 'THB', 'to': 'KRW'})

        # Assert the returned responses
        self.assertIsNotNone(self.currencyExchanger.api_response)
        self.assertEqual(self.currencyExchanger.api_response, self.mock_api_response.json())
    @patch("source.currency_exchanger.requests")
    def test_currency_exchange(self, mock_request):
        # Assign mock's return value
        self.currencyExchanger.target_currency = 'KRW'
        mock_request.get.return_value = self.mock_api_response
        # Act - execute class under test
        result = self.currencyExchanger.currency_exchange(500)
        expect = 500 * 38.69
        self.assertEqual(result,expect)

        

if __name__ == '__main__':
    unittest.main()
