# tp-tests-unitaires-api

Le projet est composé d'une API Flask comprenant une base de données SQLITE d'une table :

  users (id INTEGER, name TEXT, age INTEGER)

L'API dispose de 5 routes:

GET     /select         : Retourne l'ensemble des lignes de la table users  
GET     /select/<id>    : Retourne une ligne de la table users en fonction de l'id passé dans l'URL  
POST    /create         : Ajoute une ligne dans la table users (prend en paramètre un objet JSON comprenant le nom et l'age à ajouter)  
                          Retourne true si une ligne a été ajoutée  
PUT     /update         : Met à jour une ligne (prend en paramètre un objet JSON comprenant l'id de la ligne impacté et les nouveaux nom et  age)  
                          Retourne true si une ligne a été modifiée  
DELETE  /delete/<id>    : Supprime une ligne de la table users en fonction de l'id passé dans l'URL  
                          Retourne true si une ligne a été supprimée  


Le projet contient également un ensemble de tests pytest permettant de tester la réponse de chaque route.
