from flask import Blueprint
bp_hr = Blueprint('hr', __name__)
from . import views