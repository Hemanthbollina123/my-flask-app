from flask import Blueprint, render_template
from .models import User
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # Example: Add a user to the database
    if not User.query.first():
        user = User(username='testuser', email='test@example.com')
        db.session.add(user)
        db.session.commit()
    return render_template('index.html')
