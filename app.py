from flask import Flask, request

app = Flask(__name__)  # Debes usar Flask en mayúscula

@app.route("/", methods=["GET"])
def hello():
    """ Regresa los parametros HTTP obtenidos. """
    who = request.args.get("who", "World")
    return f"Hello {who}!\n"

# Usar solo cuando se corre localmente, cuando se despliegue en Cloud Run,
# un servidor de procesos como Gunicorn serve para el app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)  # Debes usar app.run en lugar de flask.run