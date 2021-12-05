from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('musicModel.pkl', 'rb'))

def find_similar_song(name, n=5):
    series = model[name].sort_values(ascending=False)
    series = series.drop(name)
    return series.head(n).to_frame()

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/my')
def my():
    return render_template("my.html")

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        songName = result['genre'] +'.000'+ result['selectNumber'] +'.wav'
        songList = find_similar_song(songName)
        return songList.to_html(classes='table table-striped text-center', justify='center')
        # return render_template("result.html", result = songList)

if __name__ == '__main__':
    app.run(host='0.0.0.0', post=5000, debug=True)