from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pyodbc

# # db = SQLAlchemy()
# #DB_NAME = "database.db"
# conn = pyodbc.connect('Driver={SQL Server};'
#                       'Server=DESKTOP-7OPOU5G;'
#                       'Database=QuickkartDB;'
#                       'Trusted_Connection=yes;')


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'jfsljfajfal alsfjaskljfa'
    # app.config['SQLALCHEMY_DATAASE_URI'] = 'sql:///{conn}'
    # db.init_app(app)
    
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix='/')

    return app