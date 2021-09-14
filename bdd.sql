DB:
DROP DATABASE IF EXISTS etudedecasdsflow;
CREATE DATABASE IF NOT EXISTS etudedecasdsflow CHARACTER SET 'utf8';

CREATE TABLE IF NOT EXISTS etudedecasdsflow.user (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    pseudo VARCHAR(30) NOT NULL,
    password VARCHAR(255) NOT NULL,
    dateOfBirth DATE NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS etudedecasdsflow.property (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    userId INT UNSIGNED NOT NULL,
    name VARCHAR(50) NOT NULL,
    description TEXT NOT NULL,
    typeOfProperty VARCHAR(30) NOT NULL,
    city VARCHAR(30) NOT NULL,
    room INT UNSIGNED NOT NULL,
    characteristicsOfRoom TEXT NOT NULL,
    PRIMARY KEY (id)
);

CONTENT:
INSERT INTO etudedecasdsflow.user (pseudo, password, dateOfBirth)
VALUES ('Martin', 'mdp1', '1997-11-24');
INSERT INTO etudedecasdsflow.user (pseudo, password, dateOfBirth)
VALUES ('Bob', 'mdp2', '1998-05-13');
INSERT INTO etudedecasdsflow.user (pseudo, password, dateOfBirth)
VALUES ('Lucien', 'mdp3', '1996-03-15');

INSERT INTO etudedecasdsflow.property (userId, name, description, typeOfProperty, city, room, characteristicsOfRoom)
VALUES ('1', 'Loft Comfort', 'Super loft au coeur de Paris, vue sur la Tour Eiffel', 'Appartement', 'Paris', '3', 'Cuisine, Salon, Chambre');
INSERT INTO etudedecasdsflow.property (userId, name, description, typeOfProperty, city, room, characteristicsOfRoom)
VALUES ('2', 'Loft Nul', 'Loft pas ouf', 'Appartement', 'Paris', '2', 'Cuisine, Chambre');
INSERT INTO etudedecasdsflow.property (userId, name, description, typeOfProperty, city, room, characteristicsOfRoom)
VALUES ('3', 'Maison', 'Maison comfortable', 'Maison', 'Montpellier', '4', 'Cuisine, 2 Chambre, 2 salles de bain, salon');