import os
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
if os.path.exists("env.py"):
      import env 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'photo_gallery'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        email = request.form["email"].lower()
        name = request.form["name"].lower()
        users = mongo.db.users
        existing_user = users.find_one({'email' : email})
        if existing_user:
            flash("Email already exists Please try to Login")
            return redirect(url_for("signup"))
        if existing_user is None:
            hashpass = generate_password_hash(request.form['pass'])
            users.insert({'name' : name, 
            'password' : hashpass,
            'email' : email})
            session['email'] = email
            session['logged_in'] = True
            return redirect(url_for('profile', email=email))        
    return render_template("signup.html")

@app.route('/login',methods=['POST', 'GET'])
def login():
    if request.method=="POST":
        existing_user = mongo.db.users.find_one(
            {"email":request.form["email"].lower()})
        if existing_user:
            if check_password_hash(existing_user["password"], request.form["pass"]):
                session["email"]    = request.form["email"]  
                session['logged_in'] = True
                return redirect(url_for('profile', email=request.form['email'].lower()))             
            else:
                flash("Incorrect username and/or password")
                return redirect(url_for("login"))   
        else:
            flash("This email doesn't exist in our system, kindly signup for a new account")
            return redirect (url_for("login"))
    return render_template("login.html")           

@app.route('/profile/<email>')
def profile(email):
    if session["email"].lower() == email.lower():
        existing_user = mongo.db.users.find_one(
            {"email":email.lower()})
        photos = mongo.db.photos.find({"email": email.lower()})
        return render_template("profile.html",email=email, name=existing_user["name"], photos=photos)
    else:
        flash("You are not allowed to access someone's else profile")
        return render_template("forbidden.html")

@app.route('/album/<email>')
def album(email):
    if session["email"].lower() == email.lower():
        photos = mongo.db.photos.find({"email": email.lower()})
        return render_template("album.html", photos=photos)

@app.route('/album/insert', methods=['POST'])
def album_insert():
    photos = mongo.db.photos
    inputs = request.form.to_dict()
    inputs['email'] = session['email']
    photos.insert_one(inputs)
    return redirect(url_for('album',email=session['email']))

@app.route('/logout')
def logout():
    session.pop('email')
    session.pop('logged_in')
    return render_template('index.html')


# @app.errorhandler(500)
# def page_not_found(e):
#     return render_template('forbidden.html'), 500

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)