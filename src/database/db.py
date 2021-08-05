from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_migrate import Migrate

metadata = MetaData(
    naming_convention={
        'pk': 'pk_%(table_name)s',
        'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
        'ix': 'ix_%(table_name)s_%(column_0_name)s',
        'uq': 'uq_%(table_name)s_%(column_0_name)s',
        'ck': 'ck_%(table_name)s_%(constraint_name)s',
    }
)

db = SQLAlchemy(metadata=metadata)
migrate = Migrate()

# import click
# from flask import current_app, g
# from flask.cli import with_appcontext
# import sqlite3