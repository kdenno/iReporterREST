# import flask
from flask import Blueprint, jsonify, request

from api.redflags.models import Incident
import api.redflags.statusresponse as statusresponse
from api.redflags.stoerer import store_func


# initialize blue print with module name
redendpoint = Blueprint('redflags', __name__)

redflags = store_func()

# create redflag endpoint


@redendpoint.route('/red-flags', methods=['POST'])
def create_flag():

    postdata = request.get_json()
    required_fields = ['createdBy', 'issuetype',
                       'location', 'status', 'images', 'videos', 'comment']
    if not statusresponse.check_fields(required_fields, postdata):
        return statusresponse.error_400('Required parameter(s) missing ')

    # append to redflags
    redflag = Incident(postdata)
    redflags.append(redflag)
    returnobj = redflag.to_json()

    # return to client
    return statusresponse.success_201(returnobj['id'], 'Created flag-record')

    # all redflags


@redendpoint.route('/red-flags', methods=['GET'])
def all_flags():
    if statusresponse.flag_count(redflags):
        return statusresponse.success_200([{}], 'empty')

    allredflags = statusresponse.get_flags(redflags)
    # return to client
    return statusresponse.success_200(allredflags, 'All red flags')


# get specific flag


@redendpoint.route('/red-flags/<red_flag_id>', methods=['GET'])
def get_flag(red_flag_id):

    allredflags = statusresponse.get_flags(redflags)

    for value in allredflags:
        if value.get('id') == int(red_flag_id):
            # return to client
            return statusresponse.success_200([value], 'redflag')
    else:
        return statusresponse.error_400('Flag doesnot exist')


# edit flag comment


@redendpoint.route('/red-flags/<red_flag_id>/comment', methods=['PATCH'])
def edit_flag_comment(red_flag_id):

    # check if flags
    allflags = statusresponse.get_flags(redflags)
    postdata = request.get_json()

    # check its standard
    required_fields = ['comment']
    if not statusresponse.check_fields(required_fields, postdata):
        return statusresponse.error_400('Required parameter(s) missing ')

    for index, flagdict in enumerate(allflags):
        if flagdict.get('id') == int(red_flag_id):
            # edit object data
            flagdict['comment'] = postdata['comment']

            # reconvert back to incident object
            incidentobj = Incident(flagdict)

            # replace flag
            redflags[index] = incidentobj

            # return to client
            return statusresponse.success_201(red_flag_id, 'Updated red-flag record’s commment')
    else:
        return statusresponse.error_400('Flag doesnot exist')

# edit flag location


@redendpoint.route('/red-flags/<red_flag_id>/location', methods=['PATCH'])
def edit_location(red_flag_id):

    allredflags = [flag.__dict__ for flag in redflags]
    postdata = request.get_json()

    # check its standard
    required_fields = ['location']
    if not statusresponse.check_fields(required_fields, postdata):
        return statusresponse.error_400('Required parameter(s) missing ')

    for key, value in enumerate(allredflags):
        if value.get('id') == int(red_flag_id):
            # edit object data
            value['location'] = postdata['location']

            # reconvert back to incident object
            reconverted = Incident(value)

            # replace flag
            redflags[key] = reconverted

            # return to client
            return statusresponse.success_201(red_flag_id, 'Updated red-flag record’s location')
    else:
        return statusresponse.error_400('Flag doesnot exist')


# remove flag


@redendpoint.route('/red-flags/<red_flag_id>', methods=['DELETE'])
def remove_flag(red_flag_id):

    allredflags = statusresponse.get_flags(redflags)

    for key, value in enumerate(allredflags):
        if value.get('id') == int(red_flag_id):
            # remove flag
            redflags.pop(key)

            # return to client
            return statusresponse.success_201([{'id': red_flag_id}], 'red-flag record has been deleted')
    else:
        return statusresponse.error_400('Flag doesnot exist')
