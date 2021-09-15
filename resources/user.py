from flask import request
from flask_restful import Resource
from resources.functions.functionUser import *

class Users(Resource):
    def get(self):
        return list_all_user()
        # GET : http://127.0.0.1:5000/users


class User(Resource):
    def get(self):
        id = request.args.get('id')

        return find_user_by_id(id)
        # GET : http://127.0.0.1:5000/user/id:

    def put(self):
        pseudo = request.args.get('pseudo')
        password = request.args.get('password')
        dateOfBirth = request.args.get('dateOfBirth')

        add_user(pseudo, password, dateOfBirth)
        # PUT : http://127.0.0.1:5000/property?pseudo=pseudo:&password=password:&dateOfBirth=dateOfBirth:

    def post(self):
        pseudo = request.args.get('pseudo')
        password = request.args.get('password')
        field = request.args.get('field')
        value = request.args.get('value')

        modify_user(pseudo, password, field, value)
        #POST : http://127.0.0.1:5000/user?pseudo=pseudo:&password=password:&field=field:&value=value:

    def delete(self):
        pseudo = request.args.get('pseudo')
        password = request.args.get('password')

        delete_user(pseudo, password)
        #DELETE : http://127.0.0.1:5000/user?pseudo=pseudo:&password=password: