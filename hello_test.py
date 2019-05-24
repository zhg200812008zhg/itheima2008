from flask import Flask

app = Flask(__name__, static_url_path="", static_folder="")


@app.route("/")
def index():
    return "index page"

@app.route("/order/list")
def order_list():
    return "hello order"


class Config(object):
    DEBUG = True


app.config.from_object(Config)

if __name__ == '__main__':
    app.run()
