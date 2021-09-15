from flask import request
from flask_restful import Resource
from resources.functions.functionProperty import *

class Propertys(Resource):
    def get(self):
        return list_all_property()
        # GET : http://127.0.0.1:5000/propertys


class Property(Resource):
    def get(self):
        city = request.args.get('city')

        return list_all_property_by_city(city)
        # GET : http://127.0.0.1:5000/property?city=city:

    def put(self):
        pseudo = request.args.get('pseudo')
        password = request.args.get('password')
        name = request.args.get('name')
        description = request.args.get('description')
        typeOfProperty = request.args.get('typeOfProperty')
        city = request.args.get('city')
        room = request.args.get('room')
        characteristicsOfRoom = request.args.get('characteristicsOfRoom')

        add_property(pseudo, password, name, description, typeOfProperty, city, room, characteristicsOfRoom)
        # PUT : http://127.0.0.1:5000/property?pseudo=pseudo:&password=password:&name=name:&description=description:&typeOfProperty=typeOfProperty:&city=city:&room=room:&characteristicsOfRoom=characteristicsOfRoom:

    def post(self):
        pseudo = request.args.get('pseudo')
        password = request.args.get('password')
        propertyid = request.args.get('propertyid')
        field = request.args.get('field')
        value = request.args.get('value')

        modify_property(pseudo, password, propertyid, field, value)
        #POST : http://127.0.0.1:5000/property?pseudo=pseudo:&password=password:&propertyid=propertyid:&field=field:&value=value:

    def delete(self):
        pseudo = request.args.get('pseudo')
        password = request.args.get('password')
        propertyid = request.args.get('propertyid')

        delete_property(pseudo, password, propertyid)
        #DELETE : http://127.0.0.1:5000/property?pseudo=pseudo:&password=password:&propertyid=propertyid: