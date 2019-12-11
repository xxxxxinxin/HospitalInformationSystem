from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask import redirect, request, url_for
from .config import Config
bootstrap = Bootstrap()
db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    # @app.before_request
    # def before_request():
    #     path = request.path
    #     doctorinfoid = request.cookies.get('doctorid')
    #     print(path)
    #     if doctorinfoid is None:
    #         if path == '/login' or path == '/':
    #             return
    #         else:
    #             return redirect('/login')
    #     return
    #
    # @app.before_first_request
    # def createall():
    #     print("1")
    #     db.create_all()
    #     print("2")
    app.config.from_object(Config)
    app.debug = True
    db.init_app(app)

    from .auth import bp_auth
    app.register_blueprint(bp_auth, url_prfix="/")
    from .doctor import bp_doctor
    app.register_blueprint(bp_doctor, url_prfix="/doctor")
    from .hr import bp_hr
    app.register_blueprint(bp_hr, url_prfix="/hr")
    from .nurse import bp_nurse
    app.register_blueprint(bp_nurse, url_prfix="/nurse")
    from .patient import bp_patient
    app.register_blueprint(bp_patient, url_prfix="/patient")
    from .warehouse import bp_warehouse
    app.register_blueprint(bp_warehouse, url_prfix="/warehouse")

    return app
