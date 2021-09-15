from bdd import *

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
    return userid