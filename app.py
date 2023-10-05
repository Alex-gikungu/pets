import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMYDATABASE_URL']=os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app) 

# Register routes
from routes import *

if __name__ == '__main__':
    app.run(debug=True)


# postgresql://pets_api_user:Ew7qfFyH7tuG4S7AT8RlLYYyT2pMZqjZ@dpg-ckf5ddmnpffc73cqq2gg-a.oregon-postgres.render.com/pets_api