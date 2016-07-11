#!/usr/bin/env python
import os
#from app import create_app
#from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask

COV = None
if os.environ.get('FLASK_COVERAGE'):
    import coverage
    COV = coverage.coverage(branch=True, include='app/*')
    COV.start()

if os.path.exists('.env'):
    print('Importing environment from .env...')
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]

from app import create_app


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
#manager = Manager(app)
#migrate = Migrate(app, db)




host = os.environ.get('IP', '0.0.0.0')
port = int(os.environ.get('PORT', 8080))
if __name__ == "__main__":
    app.run(host=host, port=port)