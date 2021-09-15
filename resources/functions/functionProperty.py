from bdd import *
from resources.functions.functionGeneral import *

# GET
def list_all_property():
    request = "SELECT * FROM property"
    data = execQuery(request)
    return data

def list_all_property_by_user(pseudo, password):
    currentUser = find_user_id(pseudo, password)
    request = f"SELECT * FROM property WHERE userid = '{currentUser}'"
    data = execQuery(request)
    return data

def list_all_property_by_city(ville):
    request = f"SELECT * FROM property WHERE city = '{ville}'"
    data = execQuery(request)
    return data


# PUT
def add_property(pseudo, password, name, description, typeOfProperty, city, room, characteristicsOfRoom):
    currentUser = find_user_id(pseudo, password)

    curseur = connexion.cursor()
    reference = {"userid" : currentUser, "name" : name, "description" : description , "typeOfProperty" : typeOfProperty , "city" : city , "room" : room , "characteristicsOfRoom" : characteristicsOfRoom }
    request = ("INSERT INTO property (userId, name, description, typeOfProperty, city, room, characteristicsOfRoom) VALUES(%(userid)s, %(name)s, %(description)s, %(typeOfProperty)s, %(city)s, %(room)s, %(characteristicsOfRoom)s)", reference)
    curseur.execute(*request)


# POST
def modify_property(pseudo, password, propertyid, field, value):
    currentUser = find_user_id(pseudo, password)

    curseur = connexion.cursor()
    request = f"UPDATE property SET {field} = '{value}' WHERE userid = '{currentUser}' AND id = '{propertyid}'";
    curseur.execute(request)


# DELETE
def delete_property(pseudo, password, propertyid):
    currentUser = find_user_id(pseudo, password)
    
    curseur = connexion.cursor()
    request = f"DELETE FROM property WHERE userid = '{currentUser}' AND id = '{propertyid}'";
    curseur.execute(request) 