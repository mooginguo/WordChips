from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/learning')
def learning():
    return "学習モードを選択しました"

@app.route('/review')
def review():
    return "復習モードを選択しました"

if __name__ == '__main__':
    app.run(debug=True)


