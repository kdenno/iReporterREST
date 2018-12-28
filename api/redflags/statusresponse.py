from flask import jsonify

def error_400(message):
    response = {
        'status': 400,
        'error': message
    }
    return jsonify(response), 400

def success_201(data, message):
    response = {
        'status': 201,
        'data': [{'id': data, 'message': message}]
    }
    return jsonify(response), 201


def success_200(data, message):
    response = {
        'status': 200,
        'data': data
    }
    return jsonify(response), 200

def check_fields(required_fields, postdata):
    # required_fields = ['createdBy', 'issuetype',
    #                    'location', 'status', 'images', 'videos', 'comment']
    return all(field in postdata for field in required_fields)
        
def flag_count(redflags):
    allredflags = [flag.__dict__ for flag in redflags]
    return len(allredflags) < 1

def get_flags(redflags):
    allredflags = [flag.__dict__ for flag in redflags]
    return allredflags

def check_for_ID(red_flag_id):
    if red_flag_id == '' or red_flag_id == None:
        return False


