from json import loads, dumps

from bottle import post, response, request, get, run

from service import user_service


@post('/api/users')
def add_user():
    response.content_type = 'application/json'
    request_body = loads(request.body.read())
    return dumps(
        user_service.create_user(
            request_body['username'],
            str(request_body['pw']).encode('utf-8'),
        )
    )


@post('/api/login')
def login():
    pass


@get('api/time/<user_id')
def get_time_frame(user_id):
    pass


run(host='localhost', port=8080)
