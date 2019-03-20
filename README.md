# "Restful User-Service" [![Build Status](https://travis-ci.com/mwintersperger-tgm/sew5-simple-user-database-mwintersperger-tgm.svg?branch=master)](https://travis-ci.com/mwintersperger-tgm/sew5-simple-user-database-mwintersperger-tgm)

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

Damit das programm auch als Webserver läuft muss man folgende zeilen in seinem Programm einfügen.

    # configuration
    DEBUG = True

    # instantiate the app
    app = Flask(__name__)
    app.config.from_object(__name__)

    # enable CORS
    CORS(app)

Diesen server muss man natürlich auch bei programm aufruf starten.

    if __name__ == '__main__':
      app.run(host='127.0.0.1', port=5000)


#### Imports

    from flask import Flask, jsonify, request, render_template
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

#### Making vue Static

Dammit das Programm in einer Productions umgebung verwendbar ist darf die Weboberfläche nicht immer erst mit ``npm run dev`` gestarted werden.
Als solches müssen folgende Schritte gefolgt werden dammit die Weboberfläche automatisch zusammen mit dem Flask server gestarted:

1. Ändere den static asset ordner
    Öffne /config/index.js und Ändere die Folgenden Zeilen:

            index: path.resolve(__dirname, '../dist/index.html'),
            assetsRoot: path.resolve(__dirname, '../dist'),
    zu:

            index: path.resolve(__dirname, '../../dist/index.html'),
            assetsRoot: path.resolve(__dirname, '../../dist'),
    Dies führt dazu das sich der static asset ordner auf der höhe des Frontend/Backend ordner formt.
2. Erzeuge den static asset ordner
    Hierfür einfach das build command ``npm run build`` im Backend folder ausführen.

3. Binde den static folder in das Backend ein
    Damit Flask den static folder verwenden kann muss wir ihn einbinden indem wir app = Flask wie folgt erweitert.

        app = Flask(__name__,
            static_folder = "../dist/static",
            template_folder = "../dist")

4. Rendern des Frontend
    Nun da wir den static ordner eingebunden haben, mussen wir ihn auch verwenden. Dies tun wir wie folgt:

        @app.route('/')
            def index():
            return render_template("index.html")

### Client-Desktop-Application

Die Desktop-Application befindet sich im client file um ist ein einfaches PyQT5 programm welches via requests mit dem server communiziert.

### Deploy to Production

Der HTTP server welcher standardmäßig von Flask verwendet wird ist Werkzeug.
Werkzeug ist light-weight und schnell und als solches idea für Development.
Das problem ist jedoch das Werkzeug im Klartext kommuniziert und als solches komplett nutzlos für ein Production Environment ist.
Flask weißt auf diese Tatsache mehrfach in ihrer Docu und jedes mal beim starten des Servers auf diese Tatsache hin.

Als solches muss ein anderer Server verwendet werden, was jedoch je nach server sehr schnell gehen kann.
So zum Beispiel der verwendete server Gevent muss nur mittels ``pip install gevent`` installiert werden und kann dann einfach mittel import eingebunden werden.

    from gevent.pywsgi import WSGIServer

    app = Flask(__name__)

    if __name__ == '__main__':
        http_server = WSGIServer(('', 5000), app)
        http_server.serve_forever()

## Deployment

Der server wird mit "python app.py" im server order ausgeführt.

### Weboberfläche

Die Weboberfäche wird automatisch mit dem Flask Server gestarted und befindet sich auf 127.0.0.1:5000

### Client-Desktop-Application

Die Client-Desktop-Application wird einfach mit "python gui.py" im client ordner ausgeführt. Es muss der server laufen damit sie funktionert.

### Testing 

Um Backend Testing auszuführen einfach tox im project directory eingeben.

Frontend Testing der Desktop Client Application wird ebenfalls von tox gestarted, benötigt aber einen laufenden Backend server um zu funktionieren.

Da pytest-qt nicht die fähigkeit besitzt Klicks auf die Tabelle zu simulieren benötigen alle Update und Delete Tests Manuellen User Input. Dieser user input besteht daraus auf update/delete des entsprechenden Users zu klicken.

Frontend testing  der Weboberfläche wird mittels "npx cypress open" im project directory gestarted.
Sowohl der Server als auch die weboberfläche müssen hierbei natürlich laufen.

## Quellen
[Flask Rest](https://flask-restful.readthedocs.io/en/latest/quickstart.html#full-example)

[Sqlite with Python](https://docs.python.org/3/library/sqlite3.html)

[Full-stack single page application with Vue.js and Flask](https://codeburst.io/full-stack-single-page-application-with-vue-js-and-flask-b1e036315532)

[Developing a Single Page App with Flask and Vue.js](https://testdriven.io/developing-a-single-page-app-with-flask-and-vuejs)
