from flask import Blueprint, render_template
from .forms import SignUpForm, LoginForm

auth = Blueprint('auth', __name__)


@auth.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


@auth.route("/sign-up")
def sign_up():
    form = SignUpForm()
    return render_template('signup.html', form=form)
