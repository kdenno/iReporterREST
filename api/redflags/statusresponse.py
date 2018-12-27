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

