from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():

    return """
    <h1>MiniVault</h1>

    <p>Hello Tushar</p>
    """

@app.route("/about")
def about():
    return "I'm a software Engineering student"

@app.route("/contact")
def contact():
    return "You can contact me at - tusharrbhardwaj@gmail.com"


if __name__ == "__main__":
    app.run(debug=True)