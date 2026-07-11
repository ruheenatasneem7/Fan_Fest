from flask import Flask,render_template
from flask_cors import CORS

from config import Config
from database import db

from routes.application import application_bp

app = Flask(__name__)

app.config.from_object(Config)

CORS(app)

db.init_app(app)

app.register_blueprint(application_bp)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return   render_template("index.html")
        


if __name__ == "__main__":
    app.run(debug=True)
    