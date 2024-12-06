from flask import render_templates, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from family_hub import db
from family_hub.models import User

def create_user(username, email, password, role):
    new_user = User(username=username, email=email, role=role)
    db.session.add(new_user)
    db.session.commit()

def login_user_view(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:  # Assuming you store hashed passwords
        login_user(user)
        return redirect(url_for('home'))
    else:
        flash('Login Failed! Check your credentials and try again.')

def logout_user_view():
    logout_user()
    return redirect(url_for('home'))
