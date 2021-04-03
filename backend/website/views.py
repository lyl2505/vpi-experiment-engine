from flask import Blueprint, render_template, request, session

from connection import get_connection

views = Blueprint('views', __name__)


# gets landing page
@views.route("/")
def home():
    """
    :return: index template
    """
    return render_template("index.html")


# gets experiment
@views.route("/experiment", methods=['POST', 'GET'])
def experiment():
    """
    :return: experiment render template
    """

    if request.method == 'GET':
        pass
    if request.method == 'POST'

        # get form data

        # form_data = request.form
        # age = form_data['age']

        return render_template("experiment.html")