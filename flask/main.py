"""
Import flask class
import escape to render text on browser
Note: Not call the script flask.py
"""
from crypt import methods
from flask import Flask, make_response, redirect, render_template, request, url_for, session
from markupsafe import escape
from app import create_app

"""Create an instance from app.create_app()"""
app = create_app()

"""Decorator, What URL flask should trigger(desencadenará) our function?"""
@app.route('/')
def index():
    """
        Message to display on User's browser.
        HTML is the default content type
    """
    user_ip = request.remote_addr #obtain user's ip
    response = make_response(render_template('index.html'))
    #response.set_cookie("user_ip", user_ip) #Save on cookies
    session["user_ip"] = user_ip #save data on session

    return response

@app.route("/user")
def user():
    #user_ip = request.cookies.get("user_ip") #obtain user's ip from cookies
    user_ip = session.get('user_ip')
    #names = request.cookies.get('user_name')
    names = ["1", "2"]
    context = {
        "user_ip": user_ip,
        "names": names
    }
    return render_template("user.html", **context)

@app.route("/form", methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        user_name = request.form
        #response = make_response(redirect(url_for('user')))
        response = make_response(render_template('result.html', names_user=user_name))
        #response.set_cookie('user_name', user_name)
    
        return response
    else:
        return render_template('form.html')

@app.errorhandler(404)
def not_found(error):
    """Handling error 404"""

    response = make_response(render_template('404.html', error=error))
    return response

if __name__ == '__main__':
    app.run(port = 5000, debug=True)
