from flask import Blueprint

admin = Blueprint('admin', __name__)


@admin.route("/")
def my_admin():
    return "This is ADMIN"