# "Restful User-Service"

## Aufgabenstellung
Die detaillierte [Aufgabenstellung](TASK.md) beschreibt die notwendigen Schritte zur Realisierung.

## Implementierung

### Python-Flask

Rest kann auf zwei weisen in Python implementiert werden, in klassen wie im Flask Rest Beispiel oder mit methoden wie in dieser application.
In beiden fällen werden den methoden und klassen URL adressen und CRUD befehle zugewiesen auf die sie reagieren.

    @app.route('/users', methods=['GET', 'POST']) # Annotation for the method

Da man mehrere CRUD Befehle einer methode zuweisen kann, muss diese natürlich inerhalb des programms unterscheiden können.

    if request.method == 'POST':

Da REST mit Json im hintergrund arbeitet müssen die returns der methoden zu Json umgewandelt werden und am besten mit dictionaries inerhalb der methoden gearbeited werden.

    return jsonify(response_object) # Return the dictionary response_object

Die methoden müssen natürlich auch variablen aus der adresszeile lesen können. Besagte variablen sind, wie schon erwähnt, im Json format.

    post_data = request.get_json()
    post_data.get('username') # Get the value to the key username

#### Imports

    from flask import Flask, jsonify, request
    from flask_cors import CORS

### Single-Page-Application-with-Vue.js

Vue.js ermöglicht die erzeugung einer webbasierten grafischen oberfläche für Flask applicationen.

Um ein vue.js project zu starten muss man einfach folgendes im passendem directory eingeben.

    vue init webpack <name>

Die Weboberflächen befinden sich in client/src/components.

Der router ist client/src/router/index.js und erlaubt dir den weboberflächen URL adressen zu zuweisen.

App.vue welches sich in client/src befinded ist der wrapper in dem die anderen .js dateien eigefügt werden.
Dies ist auch das file in dem man das vue.js logo entfernen kann.

Axios erlaubt vue.js die python-flask application anzusprechen.

### Client-Desktop-Application

Die Desktop-Application befindet sich im client file um ist ein einfaches PyQT5 programm welches via requests mit dem server communiziert.

## Deployment

Der server wird mit "python app.py" im server order ausgeführt.

### Weboberfläche

Om die Weboberfläche zu erzeugen muss "npm run dev" im Client ordner via CLI ausgeführt werden.

Zu finden ist sie dann auf localhost:8080

### Client-Desktop-Application

Die Client-Desktop-Application wird einfach mit "python gui.py" im client ordner ausgeführt. Es muss der server laufen damit sie funktionert.

### Testing

Um Backend Testing auszuführen einfach tox im project directory eingeben.

Frontend testing wird mittels "npx cypress open" im project directory gestarted.
Sowohl der Server als auch die weboberfläche müssen hierbei natürlich laufen.

## Quellen
[Flask Rest](https://flask-restful.readthedocs.io/en/latest/quickstart.html#full-example)

[Sqlite with Python](https://docs.python.org/3/library/sqlite3.html)

[Full-stack single page application with Vue.js and Flask](https://codeburst.io/full-stack-single-page-application-with-vue-js-and-flask-b1e036315532)

[Developing a Single Page App with Flask and Vue.js](https://testdriven.io/developing-a-single-page-app-with-flask-and-vuejs)
