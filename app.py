from flask import Flask
from api.test import test_bp
from api.auth import auth


app = Flask(__name__)
app.register_blueprint(test_bp)


@app.route("/")
def index():
    return "API uC"


if __name__=="__main__":
    app.run()
