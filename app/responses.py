from flask import jsonify


def bad_request(error):
    return jsonify({
        'success': False,
        'data': {},
        'message': 'Bad Request',
        'error': error,
        'code': 400
    }), 400


def response(data):
    return jsonify({
        'success': True,
        'data': data
    }), 200


def not_found():
    return jsonify({
        'success': False,
        'data': {},
        'message': 'Resource not found',
        'code': 404
    }), 404