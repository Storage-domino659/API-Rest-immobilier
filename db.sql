DROP DATABASE IF EXISTS etudeDeCasdsflow;
CREATE DATABASE IF NOT EXISTS etudeDeCasdsflow CHARACTER SET 'utf8';

CREATE TABLE IF NOT EXISTS etudeDeCasdsflow.user (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    pseudo VARCHAR(30) NOT NULL,
    password VARCHAR(255) NOT NULL,
    dateOfBirth DATE NOT NULL,
    city VARCHAR(30) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS etudeDeCasdsflow.property (
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

INSERT INTO etudeDeCasdsflow.user (pseudo, password, dateOfBirth, city)
VALUES ('domino', '4141', '1997-11-24', 'Paris');

INSERT INTO etudeDeCasdsflow.property (userId, name, description, typeOfProperty, city, room, characteristicsOfRoom)
VALUES ('1', 'Loft Comfort', 'Super loft au coeur de Paris, vue sur la Tour Eiffel', 'Appartement', 'Paris', '3', 'Cuisine, Salon, Balcon');