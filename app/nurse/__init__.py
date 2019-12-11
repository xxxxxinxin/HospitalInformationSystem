from flask import Blueprint
bp_nurse = Blueprint('nurse', __name__)
from . import views