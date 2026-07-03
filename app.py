from flask import Flask, render_template as webpage
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")

    hour = now.hour
    
    name = "Tushar"
    if hour >= 5 and hour <= 11:
        greet = "Good Morning"
    elif hour >= 12 and hour <= 17:
        greet = "Good Afternoon"
    else:
        greet = "Good Evening"

    return webpage("index.html",greeting = greet, time = current_time, name = name )

@app.route("/about")
def about():
    return "I'm a software Engineering student"

@app.route("/contact")
def contact():
    return "You can contact me at - tusharrbhardwaj@gmail.com"


if __name__ == "__main__":
    app.run(debug=True)