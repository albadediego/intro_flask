from flask import Flask, render_template

#Inicializar la variable app con Flask
app = Flask(__name__)

#Inicializar parámetros para el servidor de Flask
#windows: 
#set FLASK_APP=main.py

#Comando para ejecutar el servidor
#flask --app main run

#Comando para ejecutar el servidor en otro puerto diferente del default que es siempre el 5000
#flask --app main run -p 5002

#Comando para ejecutar el servidor en modo debug, para realizar cambios en código en tiempo real
#flask --app main --debug run

@app.route("/hola")
def holaMundo():
    return "Hola mundo Flask, esto es Flask, esta bueno, quiero aprender todo"

@app.route("/frutas")
def listaFrutas():
    listaFrutas = ['platano', 'fresa', 'piña', 'manzana', 'melon']
    return listaFrutas

@app.route("/dic")
def listaDic():
    listaDic = {'name':'Jose', 'email':'jose@gmail.com','name':'Maria', 'email':'maria@gmail.com'}
    return listaDic

#Tomar parametro desde ruta
@app.route("/nombre/<name>/apellido/<apellido>")
def tuNombre(name, apellido):
    return f"Hola {name} {apellido}, como estas?"

@app.route("/num/<int:parametro>")
def cuadrado(parametro):
    #parametro = int(parametro)
    return f"El cuadrado de {parametro} es {parametro*parametro}"

#Realizar una ruta que dinamicamente pueda solicitar o realizar operaciones
#de suma, resta, multiplicacion y division segun 2 parametros numericos recibidos
@app.route("/mates/<int:num1>/<int:num2>/<ope>")
def operacionesMatematicas(num1, num2, ope):
    result = None
    if ope == 'suma':
        result = f"La suma es: {num1 + num2}"
    elif ope == 'resta':
        result = f"La resta es: {num1 - num2}"
    elif ope == 'multi':
        result = f"La multiplicacion es: {num1 * num2}"
    elif ope == 'divi':
        result = f"La division es: {num1 / num2}"
    return result

@app.route("/<dato>")
def miHtml(dato):
    listaFrutas = ['platano', 'fresa', 'piña', 'manzana', 'melon']
    return render_template("hola.html", variable = dato, frutas = listaFrutas)