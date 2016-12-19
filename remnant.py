from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/photo/")
def photo():
    return render_template("photo.html")

@app.route("/video/")
def video():
    return render_template("video.html")

@app.route("/design/")
def design():
    return render_template("design.html")

if __name__ == "__main__":
    app.run()
