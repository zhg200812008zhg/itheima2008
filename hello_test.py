from flask import Flask

app = Flask(__name__, static_url_path="", static_folder="")


@app.route("/")
def index():
    return "index page"


@app.route("/cart/list")
def cartlist():
    return "cart_list"


class Config(object):
    DEBUG = True


app.config.from_object(Config)

if __name__ == '__main__':
    app.run()
