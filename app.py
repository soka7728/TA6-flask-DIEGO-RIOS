from flask import Flask, render_template, request, redirect, url_for, abort

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    resultado = None
    estado = None
    error = None

    if request.method == "POST":
        try:
            nota1 = float(request.form["nota1"])
            nota2 = float(request.form["nota2"])
            nota3 = float(request.form["nota3"])
            asistencia = float(request.form["asistencia"])
        except (ValueError, KeyError):
            error = "Debes ingresar solo números en todos los campos."
        else:
            if not (10 <= nota1 <= 70 and 10 <= nota2 <= 70 and 10 <= nota3 <= 70):
                error = "Las notas deben estar entre 10 y 70."
            elif not (0 <= asistencia <= 100):
                error = "La asistencia debe estar entre 0 y 100."
            else:
                promedio = round((nota1 + nota2 + nota3) / 3, 1)
                if promedio >= 40 and asistencia >= 75:
                    estado = "APROBADO"
                else:
                    estado = "REPROBADO"
                resultado = promedio

    return render_template("ejercicio1.html", resultado=resultado, estado=estado, error=error)


@app.route("/ejercicio1/reset")
def reset_ejercicio1():
    return redirect(url_for("ejercicio1"))


@app.route("/ejercicio2", methods=["GET", "POST"], defaults={"sugerencia": None})
@app.route("/ejercicio2/<sugerencia>", methods=["GET", "POST"])
def ejercicio2(sugerencia):
    if sugerencia is not None and sugerencia.strip() == "":
        abort(404)

    nombre_mayor = None
    cantidad = None
    error = None

    if request.method == "POST":
        nombre1 = request.form.get("nombre1", "").strip()
        nombre2 = request.form.get("nombre2", "").strip()
        nombre3 = request.form.get("nombre3", "").strip()

        if not nombre1 or not nombre2 or not nombre3:
            error = "Debes completar los 3 nombres."
        else:
            nombres = [nombre1, nombre2, nombre3]
            nombre_mayor = max(nombres, key=len)
            cantidad = len(nombre_mayor)

    return render_template(
        "ejercicio2.html",
        nombre_mayor=nombre_mayor,
        cantidad=cantidad,
        error=error,
        sugerencia=sugerencia,
    )


if __name__ == "__main__":
    app.run(debug=True)
