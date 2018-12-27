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
    self.assertEqual(data.get("message"), "Flag doesnot exist")


def test_delete_redflag(self):
    """delete red-flag with non existing id"""
    response = self.client.delete("api/v1/red-flags/3")
    data = json.loads(response.data.decode())
    self.assertEqual(response.status_code, 400)
    self.assertEqual(data.get("message"), "Flag doesnot exist")

    """delete red-flag with existing id"""
    response = self.client.delete("api/v1/red-flags/2")
    data = json.loads(response.data.decode())
    self.assertEqual(response.status_code, 201)
    self.assertEqual(data.get("message"), "red-flag record has been deleted")


# def test_create_flag_missing_params(self):
#     input_data = {'createdOn': '23-12-2018',
#                   'createdBy': 'kdenno', 'issuetype': 'red-flag', 'location': 'kamwokya', 'status': 'pending', 'images': 'images', 'videos': 'videos', 'comment': 'comment comment'}
#     response = self.app_tester.post('/api/v1/red-flags', json=input_data)
#     self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
