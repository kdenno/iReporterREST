import unittest
import json
from api import app
from api.redflags import statusresponse
from api.redflags.models import Incident


class TestValidity(unittest.TestCase):
    def setUp(self):
        self.status_response = statusresponse
        self.incident = Incident

    def test_input_fields(self):
        required_fields = ['createdBy', 'issuetype',
                        'location', 'status', 'images', 'videos', 'comment']
        post_data = {
            
            "issuetype": "red-flag",
            "location": "Kawempe",
            "status": "Pending",
            "videos": "Video url",
            "images": "images urls",
            "comment": "Caught taking bribe"}

        post_data2 = {
            "createdBy": "K-Denno",
            "issuetype": "red-flag",
            "location": "Kawempe",
            "status": "Pending",
            "videos": "Video url",
            "images": "images urls",
            "comment": "Caught taking bribe"}

        self.assertFalse(self.status_response.check_fields(required_fields, post_data))
        self.assertTrue(self.status_response.check_fields(required_fields, post_data2))   


    def test_flag_count(self):
        incident_data = {
            "createdBy": "K-Denno",
            "issuetype": "red-flag",
            "location": "Kawempe",
            "status": "Pending",
            "videos": "Video url",
            "images": "images urls",
            "comment": "Caught taking bribe"}
        new_incident = self.incident(incident_data)
        self.assertFalse(self.status_response.flag_count([new_incident]))

    def test_to_json(self):
        incident_data = {
            "id": 58,
            "createdOn": "12-1-2019",
            "createdBy": "K-Denno",
            "issuetype": "red-flag",
            "location": "Kawempe",
            "status": "Pending",
            "videos": "Video url",
            "images": "images urls",
            "comment": "Caught taking bribe"}
        new_incident = self.incident(incident_data)
        self.assertDictEqual(new_incident.to_json(), {'id': 58, 'createdOn': '12-1-2019','createdBy': 'K-Denno','issuetype': 'red-flag','location': 'Kawempe','status': 'Pending','videos': 'Video url', 'images': 'images urls', 'comment': 'Caught taking bribe'})

     
        


if __name__ == '__main__':
    unittest.main()
