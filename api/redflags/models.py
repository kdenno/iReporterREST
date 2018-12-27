import random
import datetime


class Incident():
    def __init__(self, postdata):
        if postdata.get('id'):
            self.id = postdata.get('id')
        else:
            self.id = random.randrange(1, 100)
        self.createdOn = datetime.datetime.now()
        self.createdBy = postdata.get("createdBy")
        self.issuetype = postdata.get("issuetype")
        self.location = postdata.get("location")
        self.status = postdata.get("status")
        self.images = postdata.get("images")
        self.videos = postdata.get("videos")
        self.comment = postdata.get("comment")

    def to_json(self):
        return {'id': self.id, 'createdOn': self.createdOn, 'createdBy': self.createdBy, 'issuetype': self.issuetype, 'location': self.location, 'status': self.status, 'images': self.images, 'videos': self.videos, 'comment': self.comment}

    # def __repr__(self):
    #     return str(self.__dict__)
