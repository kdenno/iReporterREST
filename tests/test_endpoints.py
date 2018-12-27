import unittest
import json
from api import app


class TestEndpoints(unittest.TestCase):
    def setUp(self):
        self.app_tester = app.test_client(self)

    def test_create_flags(self):
        input_data = {

            "createdBy": "Jon Mark",
            "issuetype": "red-flag",
            "location": "Kawempe",
            "status": "Pending",
            "videos": "Video url",
            "images": "images urls",
            "comment": "He was caught red handed"}

        response = self.app_tester.post('/api/v1/red-flags', json=input_data)
        self.assertEqual(response.status_code, 201)

    def test_all_flags(self):

        response = self.app_tester.get('/api/v1/red-flags')
        #data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(len(data['data']), 2)
        #self.assertEqual(data['data'][0]['location'], 'kamwokya')
        #self.assertEqual(data['data'][0]['id'], '1')

    def test_get_specific_flag(self):
        """Test get redflag with with non existing id"""
        response = self.app_tester.get("api/v1/red-flags/19")
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data.get("error"), "Flag doesnot exist")

    def test_delete_redflag(self):
        """delete red-flag with non existing id"""
        response = self.app_tester.delete("api/v1/red-flags/3")
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)

        self.assertIn(data.get("error"), "Flag doesnot exist")


if __name__ == '__main__':
    unittest.main()
