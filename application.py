from flask import Flask, render_template

app = Flask(__name__)

# 単語データの例
words = [
    {'word': 'apple', 'meaning': 'a fruit', 'etymology': 'Latin', 'synonyms': ['fruit', 'orchard'], 'antonyms': ['vegetable'], 'example': 'I eat an apple every day.', 'mnemonic': 'An apple a day keeps the doctor away.'},
    {'word': 'banana', 'meaning': 'a yellow fruit', 'etymology': 'Arabic', 'synonyms': ['fruit'], 'antonyms': ['vegetable'], 'example': 'Bananas are rich in potassium.', 'mnemonic': 'Bananas are yellow like the sun.'},
    # 他の単語データ...
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/learning/<int:word_index>')
def learning(word_index):
    # 現在の単語を取得
    current_word = words[word_index]

    # 次の単語のインデックス（循環させる）
    next_index = (word_index + 1) % len(words)
    prev_index = (word_index - 1) % len(words)

    return render_template('learning.html',
                           word_data=current_word,
                           next_index=next_index,
                           prev_index=prev_index)

@app.route('/review/<int:word_index>')
def review(word_index):
    # 現在の単語を取得
    current_word = words[word_index]

    # 次の単語のインデックス（循環させる）
    next_index = (word_index + 1) % len(words)
    prev_index = (word_index - 1) % len(words)

    return render_template('learning.html',
                           word_data=current_word,
                           next_index=next_index,
                           prev_index=prev_index)

if __name__ == '__main__':
    app.run(debug=True)
