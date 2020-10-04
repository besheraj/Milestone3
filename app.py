import os, time
import boto3, botocore
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask import Flask, render_template, redirect, request, url_for, session, flash 
from flask_paginate import Pagination, get_page_parameter
from flask_pymongo import PyMongo , pymongo
from bson.objectid import ObjectId 
from functools import wraps
if os.path.exists("env.py"):
      import env 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'photo_gallery'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.secret_key = os.getenv("SECRET_KEY")
S3_BUCKET = os.getenv("S3_BUCKET")
S3_LOCATION = os.getenv('S3_LOCATION')
ALLOWED_EXTENSIONS = set([ 'png', 'jpg', 'jpeg', 'gif'])
mongo = PyMongo(app)
s3 = boto3.client(
   "s3",
   aws_access_key_id=os.getenv('S3_KEY'),
   aws_secret_access_key=os.getenv('S3_SECRET')
)
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "email" in session and session["email"] is not None:
            return f(*args, **kwargs)
        return redirect(url_for('login', next=request.url))
    return decorated_function

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
@login_required
def profile(email):
    if session["email"].lower() == email.lower():
        existing_user = mongo.db.users.find_one(
            {"email":email.lower()})
        name=existing_user["name"]
        photos = mongo.db.photos.find({"email": email.lower()})
        return render_template("profile.html",email=email, name=name, photos=photos)
    else:
        flash("You are not allowed to access someone's else profile")
        return render_template("forbidden.html")

@app.route('/album')
@login_required
def album():
    email = session["email"]
    page = request.args.get(get_page_parameter(), type=int, default=1) 
    if page <= 0:
        page = 1  
    per_page = 6
    existing_user = mongo.db.users.find_one({"email":email.lower()})
    name=existing_user["name"]
    photos = mongo.db.photos.find({"email": email.lower()}).skip((page-1)*per_page).limit(per_page)
    pagination = Pagination(page=page, total=photos.count(),record_name='photos', per_page=per_page)
    return render_template("album.html", photos=photos , pagination=pagination,name=name )

def upload_file_to_s3(file, bucket_name, acl="public-read"):
    try:
        file_name = str(time.time()) + "-" + file.filename
        s3.upload_fileobj(
            file,
            bucket_name,
            file_name,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            })
    except Exception as e:
        print("Something Happened: ", e)
        return e
    return "{0}{1}".format(S3_LOCATION, file_name)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/album/insert', methods=['POST'])
@login_required
def album_insert():
    if request.method == 'POST':
        if "user_file" not in request.files:
            flash("No user_file key in request.files")
            return redirect(url_for('profile', email=session['email']))   

        file = request.files["user_file"]
        if file.filename == "":
            flash("Please select a file")
            return redirect(url_for('profile', email=session['email']))

        if file and allowed_file(file.filename):
            file.filename = secure_filename(file.filename)
            src = upload_file_to_s3(file, S3_BUCKET)
        else:
            flash("we only accept photos with the following extentions png, jpg, jpeg, gif")
            return redirect(url_for('profile', email=session['email']))
        photos = mongo.db.photos
        inputs = {"email": session["email"], "src": src, "alt": request.form["alt"]}
        photos.insert_one(inputs)
        return redirect(url_for('album',email=session['email']))

@app.route('/logout')
@login_required
def logout():
    session.pop('email')
    session.pop('logged_in')
    return render_template('index.html')

@app.route('/delete_photo/<photo_id>')
@login_required
def delete_photo(photo_id):
    photo = mongo.db.photos.find_one({'_id': ObjectId(photo_id)})
    src = photo["src"].replace(S3_LOCATION, "")
    s3.delete_object(Bucket=S3_BUCKET,Key=src)
    mongo.db.photos.remove({'_id': ObjectId(photo_id)})
    return redirect(url_for('album',email=session['email']))

@app.route('/edit_my_profile')
def edit_my_profile():
    return render_template("edit_my_profile.html")


# @app.errorhandler(500)
# def page_not_found(e):
#     return render_template('forbidden.html'), 500

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)