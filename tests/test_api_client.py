import unittest
from api_client import summarize_users


class ApiClientTests(unittest.TestCase):
    def test_summarize_users_extracts_expected_fields(self):
        users = [{
            "id": 1,
            "name": "Leanne Graham",
            "username": "Bret",
            "email": "sincere@example.com",
            "address": {"city": "Gwenborough"}
        }]
        result = summarize_users(users)
        self.assertEqual(result[0]["id"], 1)
        self.assertEqual(result[0]["city"], "Gwenborough")
        self.assertEqual(result[0]["name"], "Leanne Graham")


if __name__ == "__main__":
    unittest.main()
