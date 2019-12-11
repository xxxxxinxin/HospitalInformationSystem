from flask import Blueprint
bp_patient = Blueprint('patient', __name__)
from . import views