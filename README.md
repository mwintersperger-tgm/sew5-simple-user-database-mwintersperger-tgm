# "Restful User-Service"

## Aufgabenstellung
Die detaillierte [Aufgabenstellung](TASK.md) beschreibt die notwendigen Schritte zur Realisierung.

## Implementierung


### Deployment

Bevor das programm verwendet werden kann muss createDB.py ausgeführt werden um die Datenbank aufzusetzen und "npm run dev" im Client ordner via CLI ausgeführt werden um die grafische Oberfläche zu erzeugen.

Der server wird mit "python app.py" im server order ausgeführt.

### Grafische Oberfläche

Befindet sich auf localhost:8080.

### Testing

Um Testing auszuführen einfach npx cypress open eingeben

## Quellen
[Flask ReST](https://flask-restful.readthedocs.io/en/latest/quickstart.html#full-example)
[Sqlite with Python](https://docs.python.org/3/library/sqlite3.html)
[Full-stack single page application with Vue.js and Flask](https://codeburst.io/full-stack-single-page-application-with-vue-js-and-flask-b1e036315532)
[Developing a Single Page App with Flask and Vue.js](https://testdriven.io/developing-a-single-page-app-with-flask-and-vuejs)
