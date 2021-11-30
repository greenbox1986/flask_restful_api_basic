from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from db import db
from security import authenticate, identity
from resources.user import UserRegister, User
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://nqhhlfuozdepub:c7287309c7bbd3992f7bf09a26a468a8c68e3a9a3604bf4591cbdab91444da5c@ec2-34-224-117-67.compute-1.amazonaws.com:5432/d2v59spqrh0hm0'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'
jwt = JWTManager(app)  # /auth
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:user_id>')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
