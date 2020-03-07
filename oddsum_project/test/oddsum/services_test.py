import requests
import unittest


class OddSumServiceTest(unittest.TestCase):
    """ Test class for the OddSum service. Make sure the service is running before executing the tests."""

    def test_something(self):
        """Test the service with different inputs."""
        url = 'http://localhost:55002/oddsum'

        data = {'number1': 1, 'number2': 3}
        response = requests.post(url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.text), "4")

        data = {'number1': 2, 'number2': 3}
        response = requests.post(url, data=data)
        self.assertEqual(response.status_code, 400)

        data = {'number1': 2, 'number2': 4}
        response = requests.post(url, data=data)
        self.assertEqual(response.status_code, 400)

        data = {'number1': 1, 'number2': 4}
        response = requests.post(url, data=data)
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
