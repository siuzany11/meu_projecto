from flask import Blueprint, render_template, request, redirect, url_for
# from werkzeug.security import check_password_hash, generate_password_hash

from . import db
from .models import studentii
from flask_login import login_required, login_user, logout_user


auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html")
# @auth.route('/login', methods=['GET', 'POST'])
# def login():
#     msg = ''
#     email = request.form.get('email')
#     password = request.form.get('password')
#     user = studentii.query.filter_by(email=email).first()
#     if request.method == 'POST':
#         if user:
#             if user.password == password:
#                 login_user(user, remember=True)
#                 return redirect(url_for('views.home'))
#             else:
#                 msg = 'Password incorrect!!'
#         else:
#             msg = 'Email does not exist!!'
#     return render_template('home.html', msg=msg)


@auth.route('/home')
def home():
    return render_template("home.html")

@auth.route('/form')
def form():
    return render_template("form1.html")

@auth.route('/fomular')
def fomlar():
    return render_template("form2.html")

@auth.route('/alege')
def alege():
    return render_template("alege.html")

@auth.route('/discipline')
def discipline():
    return render_template("discipline.html")
@auth.route('/contact')
def contact():
    return render_template("contact.html")

@auth.route('/about')
def about():
    return render_template("about.html")

@auth.route('/logout')
def logout():
    return render_template("login.html")
