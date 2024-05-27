# app.py
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#from models import User, Betaregistration


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/beta')
def betapage():
    return render_template('UserRegistration.html')


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(16), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username



class Betaregistration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(16), nullable=False)
    address = db.Column(db.String(500), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    new_user = User(username=username, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('index'))



@app.route('/beta', methods=['POST'])
def registerbeta():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    address = request.form['address']
    new_user = Betaregistration(username=username, email=email, password=password, address=address)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('betapage'))


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
