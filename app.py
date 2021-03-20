from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0



@app.route("/") 
def home():
    return render_template("home.html")

@app.route("/companies") 
def companies():
    return render_template("companies.html")


if __name__ == "__main__":
    app.run(debug=True)
