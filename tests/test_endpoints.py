import unittest
import json
from api import app


class TestEndpoints(unittest.TestCase):
    def setUp(self):
        self.app_tester = app.test_client(self)

    def test_create_flags(self):
        input_data = {

            "createdBy": "K Denno",
            "issuetype": "red-flag",
            "location": "Kawempe",
            "status": "Pending",
            "videos": "Video url",
            "images": "images urls",
            "comment": "Caught taking bribe"}

        response = self.app_tester.post('/api/v1/red-flags', json=input_data)
        self.assertEqual(response.status_code, 201)

    
    def test_all_flags(self):

        response = self.app_tester.get('/api/v1/red-flags')
        data = json.loads(response.data.decode())        
        self.assertEqual(response.status_code, 200)
        

    def test_get_specific_flag(self):
        """Test get redflag with with non existing id"""
        response = self.app_tester.get("api/v1/red-flags/19")
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data.get("error"), "Flag doesnot exist")


    def test_edit_flag_comment(self):
        """Test edit redflag comment with with non existing id"""
        input_data = {

            "createdBy": "K Denno",
            "issuetype": "red-flag",
            "location": "Kawempe",
            "status": "Pending",
            "videos": "Video url",
            "images": "images urls",
            "comment": "Caught taking bribe"}
        response = self.app_tester.patch("api/v1/red-flags/19/comment", json=input_data)
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)             
        self.assertEqual(data["error"], "Flag doesnot exist")


    def test_edit_flag_location(self):
        """Test edit redflag comment with with non existing id"""
        input_data = {

            "createdBy": "K Denno",
            "issuetype": "red-flag",
            "location": "Kawempe",
            "status": "Pending",
            "videos": "Video url",
            "images": "images urls",
            "comment": "Caught taking bribe"}
        response = self.app_tester.patch("api/v1/red-flags/19/location", json=input_data)
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)             
        self.assertEqual(data["error"], "Flag doesnot exist")


    def test_delete_redflag(self):
        """delete red-flag with non existing id"""
        response = self.app_tester.delete("api/v1/red-flags/3")
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)

        self.assertIn(data.get("error"), "Flag doesnot exist")


if __name__ == '__main__':
    unittest.main()
