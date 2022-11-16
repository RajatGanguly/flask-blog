from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/flask_ganguly"
db = SQLAlchemy(app)

class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    message = db.Column(db.String(120), nullable=False)
    time = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route("/post")
def post():
    return render_template("post.html")
app.run(debug=True)