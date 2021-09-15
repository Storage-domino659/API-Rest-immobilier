from bdd import *
from datetime import datetime
from resources.functions.functionGeneral import *

# GET
def find_user_by_id(id):
    request = f"SELECT * FROM user WHERE id = '{id}'"
    data = execQuery(request)
    return data

def list_all_user():
    request = "SELECT * FROM user"
    data = execQuery(request)
    #Convertis la date en isoformat pour qu'elle soit lisible en JSON
    for key in data.keys():
        record = data[key]
        record['dateOfBirth'] = datetime.strptime(record['dateOfBirth'], '%Y-%m-%d').isoformat()
    return data


# PUT
def add_user(pseudo, password, dateOfBirth):

    curseur = connexion.cursor()
    reference = {"pseudo" : pseudo, "password" : password, "dateOfBirth" : dateOfBirth }
    request = ("INSERT INTO user (pseudo, password, dateOfBirth) VALUES(%(pseudo)s, %(password)s, %(dateOfBirth)s)", reference)
    curseur.execute(*request)


# POST
def modify_user(pseudo, password, field, value):
    currentUser = find_user_id(pseudo, password)
 
    curseur = connexion.cursor()
    request = f"UPDATE user SET {field} = '{value}' WHERE id = '{currentUser}'";
    curseur.execute(request)


# DELETE
def delete_user(pseudo, password):
    currentUser = find_user_id(pseudo, password)
    
    curseur = connexion.cursor()
    request = f"DELETE FROM user WHERE id = '{currentUser}'";
    request2 = f"DELETE FROM property WHERE userid = '{currentUser}'";
    curseur.execute(request)
    curseur.execute(request2)
    