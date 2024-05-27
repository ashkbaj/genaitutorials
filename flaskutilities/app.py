from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)


@app.route('/submit_form', methods=['POST'])
def submit_form():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    new_user = User(username=username, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

    return f"User {username} registered successfully!"


if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)

#db.create_all()  # Create database tables
#app.run(debug=True)
