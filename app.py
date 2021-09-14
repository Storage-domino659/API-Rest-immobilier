from resources.bdd import *

#User
def list_all_user():
    request = "SELECT * FROM user"
    curseur = connexion.cursor()
    curseur.execute(request)

    users = curseur.fetchall()

    for user in users:
        print(user)


def modify_user(arg, value):
    TODDO


#Property
def list_all_property():
    request = "SELECT * FROM property"
    curseur = connexion.cursor()
    curseur.execute(request)

    propertys = curseur.fetchall()

    for property in propertys:
        print(property)


def list_all_property_by_city(ville):
    request = f"SELECT * FROM property WHERE city = '{ville}'"
    curseur = connexion.cursor()
    curseur.execute(request)

    propertys = curseur.fetchall()

    for property in propertys:
        print(property)

cityname = 'Montpellier'


def modify_property(arg, value):
    TODDO


def add_property(value):
    TODDO


# list_all_user()
# list_all_property()
list_all_property_by_city(cityname)


