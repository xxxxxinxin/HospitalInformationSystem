from flask import Blueprint
bp_warehouse = Blueprint('warehouse', __name__)
from . import views