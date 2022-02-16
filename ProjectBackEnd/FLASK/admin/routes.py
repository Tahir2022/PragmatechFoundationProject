from run import app, render_template


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/rooms")
def rooms():
    return render_template("/room.html")

@app.route("/contact")
def contact():
    return render_template("/contact.html")

@app.route("/city")
def city():
    return render_template("city.html")