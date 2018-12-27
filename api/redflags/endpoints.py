# import flask
from flask import Blueprint, jsonify, request

from api.redflags.models import Incident
import api.redflags.statusresponse as statusresponse
from api.redflags.stoerer import store_func


# init blue print with current module name
redendpoint = Blueprint('redflags', __name__)

redflags = store_func()

# create redflag endpoint


@redendpoint.route('/red-flags', methods=['POST'])
def create_flag():

    postdata = request.get_json()
    # check for data
    if not postdata:
        return statusresponse.error_400('No data posted')

    # check its standard
    required_fields = ['createdBy', 'issuetype',
                       'location', 'status', 'images', 'videos', 'comment']
    if not all(field in postdata for field in required_fields):
        return statusresponse.error_400('Required paremeter(s) missing')

    # append to redflags
    redflag = Incident(postdata)
    redflags.append(redflag)
    returnobj = redflag.to_json()

    # return to client
    return statusresponse.success_201(returnobj['id'], 'Created flag-record')
