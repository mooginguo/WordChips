from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/learning')
def learning():
    # 学習モードのページに遷移
    word_data = {
        'word': 'study',
        'meaning': 'to learn about a subject, usually at school or university',
        'etymology': 'from Latin "studium" meaning zeal, devotion',
        'synonyms': ['learn', 'examine', 'research'],
        'antonyms': ['neglect', 'ignore'],
        'example': 'She is studying hard for her exams.',
        'mnemonic': 'Think of studying as "steady" work towards your goal.'
    }
    return render_template('learning.html', word_data=word_data)

@app.route('/review')
def review():
    return "復習モードを選択しました"

if __name__ == '__main__':
    app.run(debug=True)

