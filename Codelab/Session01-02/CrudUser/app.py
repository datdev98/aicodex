from flask import Flask
from config import Config
from sqlite import db
from users.views import users_bp
from flask_migrate import Migrate
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(users_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()