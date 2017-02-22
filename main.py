from flask import Flask
import flask_login
import flask
from flask_pymongo import PyMongo



app = Flask(__name__)

app.secret_key = "This is secret"
app.config["MONGO_DBNAME"] = "b"
mongo = PyMongo(app)


@app.route("/")
def index():

    return "Hello"


@app.route('/users')
def users():
    users =  mongo.db.users.find()
    return flask.render_template('Users.html', users=users)

@app.route('/donors')
def donors():
    donors = mongo.db.donors.find()
    return flask.render_template('Donors.html', donors=donors)

@app.route('/posts')
def posts():
    posts = mongo.db.posts.find()
    return flask.render_template('Posts.html', posts=posts)

@app.route('/block/<fb_id>')
def block(fb_id):
    mongo.db.users.update_one(
        {
            "facebook_id":fb_id
        },
        {
            "$set":{
                "activate":0
            }
        }
    )
    return flask.redirect(flask.url_for('users'))

@app.route('/unblock/<fb_id>')
def unblock(fb_id):
    mongo.db.users.update_one(
        {
            "facebook_id":fb_id
        },
        {
            "$set":{
                "activate":1
            }
        }
    )
    return flask.redirect(flask.url_for('users'))
@app.route('/dashboard')
def dashboard():
    no_of_users = mongo.db.users.count()
    no_of_posts = mongo.db.posts.count()
    no_of_donors = mongo.db.donors.count()
    no_of_reports = mongo.db.reports.count()
    return flask.render_template('Home.html', no_of_users=no_of_users, no_of_posts=no_of_posts, no_of_donors=no_of_donors,
                                 no_of_reports=no_of_reports)

if __name__ == "__main__":
    app.run(port=1234)
