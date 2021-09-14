from resources.bdd import *

#User
# GET
def find_user_id(pseudo, password):
    request = f"SELECT id FROM user WHERE pseudo = '{pseudo}' AND password  = '{password}'"
    curseur = connexion.cursor()
    curseur.execute(request)
    id = curseur.fetchall()
    userid = id[0][0]
    # print(userid)
    return userid


def list_all_user():
    request = "SELECT * FROM user"
    curseur = connexion.cursor()
    curseur.execute(request)
    users = curseur.fetchall()
    connexion.close()

    for user in users:
        print(user)


# POST
def modify_user(pseudo, password, field, value):
    currentUser = find_user_id(pseudo, password)
    print(currentUser)
 
    curseur = connexion.cursor()
    request = f"UPDATE user SET {field} = '{value}'  WHERE id = '{currentUser}'";
    curseur.execute(request)
    connexion.close()


#Property
# GET
def list_all_property():
    request = "SELECT * FROM property"
    curseur = connexion.cursor()
    curseur.execute(request)
    propertys = curseur.fetchall()
    connexion.close()

    for property in propertys:
        print(property)


def list_all_property_by_user(pseudo, password):
    currentUser = find_user_id(pseudo, password)
    # print(currentUser)

    request = f"SELECT * FROM property WHERE userid = '{currentUser}'"
    curseur = connexion.cursor()
    curseur.execute(request)
    propertys = curseur.fetchall()
    connexion.close()

    for property in propertys:
        print(property)


def list_all_property_by_city(ville):
    request = f"SELECT * FROM property WHERE city = '{ville}'"
    curseur = connexion.cursor()
    curseur.execute(request)
    propertys = curseur.fetchall()
    connexion.close()

    for property in propertys:
        print(property)


# PUT
def add_property(pseudo, password, name, description, typeOfProperty, city, room, characteristicsOfRoom):
    currentUser = find_user_id(pseudo, password)
    # print(currentUser)

    curseur = connexion.cursor()
    reference = {"userid" : currentUser, "name" : name, "description" : description , "typeOfProperty" : typeOfProperty , "city" : city , "room" : room , "characteristicsOfRoom" : characteristicsOfRoom }
    request = ("INSERT INTO property (userId, name, description, typeOfProperty, city, room, characteristicsOfRoom) VALUES(%(userid)s, %(name)s, %(description)s, %(typeOfProperty)s, %(city)s, %(room)s, %(characteristicsOfRoom)s)", reference)
    curseur.execute(*request)
    connexion.close()


# POST
def modify_property(pseudo, password, propertyid, field, value):
    currentUser = find_user_id(pseudo, password)
    print(currentUser)
 
    curseur = connexion.cursor()
    request = f"UPDATE property SET {field} = '{value}' WHERE userid = '{currentUser}' AND id = '{propertyid}'";
    curseur.execute(request)
    connexion.close()


# DELETE
def delete_property(pseudo, password, propertyid):
    currentUser = find_user_id(pseudo, password)
    # print(currentUser)

    curseur = connexion.cursor()
    request = f"DELETE FROM property WHERE userid = '{currentUser}' AND id = '{propertyid}'";
    curseur.execute(request)
    connexion.close()


# find_user_id('Lucien', 'mdp3')
# list_all_user()
# list_all_property()
# cityname = 'Montpellier'
# list_all_property_by_city(cityname)
# add_property('Lucien', 'mdp3', 'Maison test', 'Ca va marcher', 'Test', 'Paris', '1', 'supertest')
# modify_property('Lucien', 'mdp3', 22, 'name', 'kawabonga')
# modify_user('Lucien', 'mdp3', 'pseudo', 'Lulu')
# list_all_property_by_user('Lulu', 'mdp3')
# delete_property('Lulu', 'mdp3', 25)