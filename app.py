from flask import Flask

app = Flask(__name__)
@app.route('/')
def indix():
    return "<h1> hello word </h1>"

if __name__ == '__main__':
    app.run()
