from flask import Blueprint
bp_doctor = Blueprint('doctor', __name__)
from . import views