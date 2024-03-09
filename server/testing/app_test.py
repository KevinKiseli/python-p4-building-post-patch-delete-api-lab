
from flask import Flask
from models import db, Bakery, BakedGood

class TestApp:
    def setup_method(self, method):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        db.init_app(app)
        with app.app_context():
            db.create_all()

        self.app = app

    def test_creates_baked_goods(self):
        with self.app.app_context():
            # Your test logic here
            af = BakedGood.query.filter_by(name="Apple Fritter").first()
