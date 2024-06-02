from flask import Flask

app = Flask(__name__)

@app.route("/hola")
def hola():
    return "hola mundo"



@app.route("/chau")
def goodbay():
    return "chau bro"


nombre = str(input())

@app.route("/ruta/", defaults={"nombre":None})
@app.route("/ruta/<nombre>")


def func(nombre):
    return "hola " + nombre


app.run()