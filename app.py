from flask import Flask, render_template
import random
app = Flask(__name__)

meals = ["kerkyra", "corvin sushi", "bamba marha", "thai"]

@app.route("/")
def meal():
    return render_template("main.html", meal=random.choice(meals))

app.run()
