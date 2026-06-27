from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    current_time = datetime.now().strftime("%H:%M:%S")

    return f"""
    <h1>MiniVault</h1>

    <p>Hello Tushar :)</p>
    <p> <h2> current time is {current_time} </h2> </p>
    """

@app.route("/about")
def about():
    return "I'm a software Engineering student"

@app.route("/contact")
def contact():
    return "You can contact me at - tusharrbhardwaj@gmail.com"


if __name__ == "__main__":
    app.run(debug=True)