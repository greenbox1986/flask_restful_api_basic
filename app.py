import os

from flask import Flask, render_template
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
DATABASE_DEFAULT = 'postgres://nqhhlfuozdepub:c7287309c7bbd3992f7bf09a26a468a8c68e3a9a3604bf4591cbdab91444da5c@ec2-34-224-117-67.compute-1.amazonaws.com:5432/d2v59spqrh0hm0'
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL',DATABASE_DEFAULT)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', DATABASE_DEFAULT)#'sqlite:///data.db' ,
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.secret_key = 'Ehsan'
api = Api(app)

jwt = JWT(app, authenticate, identity) #/auth
   
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
