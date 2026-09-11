from flask import Flask

try:
    from flask_migrate import Migrate  # type: ignore[reportMissingModuleSource]
except ModuleNotFoundError:
    class Migrate:
        def __init__(self, *args, **kwargs):
            pass

from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(port=5555, debug=True)