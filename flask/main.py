"""
Import flask class
import escape to render text on browser
Note: Not call the script flask.py
"""
from crypt import methods
from pyexpat.errors import messages
from flask import (
    Flask,
    make_response,
    redirect,
    render_template,
    request,
    url_for,
    # session,
    flash,
)
from flask_mysqldb import MySQL
from markupsafe import escape
from app import create_app

"""Create an instance from app.create_app()"""
app = create_app()

"""Mysql connection"""
mysql = MySQL(app)

"""Decorator, What URL flask should trigger(desencadenará) our function?"""


@app.route("/")
def index():
    """
    Message to display on User's browser.
    HTML is the default content type
    """
    user_ip = request.remote_addr  # obtain user's ip
    response = make_response(render_template("index.html"))
    # response.set_cookie("user_ip", user_ip) #Save on cookies
    # session["user_ip"] = user_ip  # save data on session

    return response


@app.route("/user")
def user():
    """user_ip = request.cookies.get("user_ip") #obtain user's ip from cookies
    user_ip = session.get("user_ip")
    names = request.cookies.get('user_name')
    names = ["1", "2"]
    context = {"user_ip": user_ip, "names": names}"""
    # Get data from mysql
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    return render_template("user.html", users=data)


@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        form_result = request.form
        user_name = request.form["name"]
        user_age = request.form["age"]
        user_color = request.form["color"]

        # Mysql conection
        cursor = mysql.connection.cursor()
        # Escribimos la consulta
        cursor.execute(
            "INSERT INTO users (name, age, color) VALUES(%s, %s, %s)",
            (user_name, user_age, user_color),
        )
        # Ejecutamos la consulta, es decir, se guardan los datos en la base de datos
        mysql.connection.commit()

        # response = make_response(redirect(url_for('user')))
        # response = make_response(render_template("result.html", names_user=form_result))
        message = "User saved succesfully"
        # response = make_response(render_template("form.html", message=message))
        flash(message)  # send message to form.html
        response = make_response(redirect(url_for("form")))
        # response.set_cookie('user_name', user_name)
        print(
            "name: {0} - age: {1} - color: {2}".format(user_name, user_age, user_color)
        )

        return response
    else:
        return render_template("form.html")


@app.route("/delete/<string:id>", methods=["POST", "GET"])
def delete(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM users WHERE id={0}".format(id))
    mysql.connection.commit()
    return redirect(url_for("user"))


@app.route("/edit/<string:id>", methods=["GET"])
def edit(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM users WHERE id={0}".format(id))
    data = cursor.fetchall()
    return make_response(render_template("form.html", user_edit=data[0]))


@app.route("/update/<id>", methods=["POST"])
def update(id):
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        color = request.form["color"]
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            UPDATE users
            SET name = %s,
                age = %s,
                color = %s
            WHERE id = %s
        """,
            (name, age, color, id),
        )
        flash("Contact Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for("user"))


@app.errorhandler(404)
def not_found(error):
    """Handling error 404"""

    response = make_response(render_template("404.html", error=error))
    return response


if __name__ == "__main__":
    app.run(port=5000, debug=True)
