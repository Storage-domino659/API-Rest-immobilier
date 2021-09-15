from flask import Flask
from flask_restful import Api
from resources.user import *
from resources.property import *

app = Flask(__name__)
api = Api(app)

# URL endpoints
api.add_resource(Users, '/users', methods=['GET'])
api.add_resource(User, '/user', methods=['GET', 'PUT', 'POST', 'DELETE'])
api.add_resource(Propertys, '/propertys', methods=['GET',])
api.add_resource(Property, '/property', methods=['GET', 'PUT', 'POST', 'DELETE'])

# Lancement Appli
if __name__ == '__main__':
    app.run()