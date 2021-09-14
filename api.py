from resources.bdd import *
from datetime import datetime
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


def execQuery(query):
    curseur = connexion.cursor()
    curseur.execute(query)
    dataSet = curseur.fetchall()
    #Permet de récuperer les légendes de la db SQL
    fields = curseur.description
    #Met le résultat sous la forme de dictionnaire
    i=0
    j=0
    result={}
    resultSet={}
    for data in dataSet:
            i=0
            for field in fields:
                    if i<data.__len__():
                            result[field[0]]=str(data[i])
                            i+=1
            resultSet[j] = result.copy()
            j+=1
    return resultSet

def find_user_id(pseudo, password):
    request = f"SELECT id FROM user WHERE pseudo = '{pseudo}' AND password  = '{password}'"
    curseur = connexion.cursor()
    curseur.execute(request)
    id = curseur.fetchall()
    userid = id[0][0]
    # print(userid)
    return userid


class Users(Resource):
    def get(self):
        request = "SELECT * FROM user"
        data = execQuery(request)
        print(data)
        #Convertis la date en isoformat pour qu'elle soit lisible en JSON
        for key in data.keys():
            record = data[key]
            record['dateOfBirth'] = datetime.strptime(record['dateOfBirth'], '%Y-%m-%d').isoformat()
        return data








# Add URL endpoints
api.add_resource(Users, '/users')

if __name__ == '__main__':
    app.run()