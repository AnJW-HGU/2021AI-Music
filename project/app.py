from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/my')
def my():
    return render_template("my.html")

if __name__ == '__main__':
    app.run(debug=True)