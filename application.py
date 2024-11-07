from flask import Flask, render_template

app = Flask(__name__)

# 単語データの例
words = [
    {'word': 'apple', 'meaning': 'a fruit', 'etymology': 'Latin', 'synonyms': ['fruit', 'orchard'], 'antonyms': ['vegetable'], 'example': 'I eat an apple every day.', 'mnemonic': 'An apple a day keeps the doctor away.', 'is_completed':True},
    {'word': 'banana', 'meaning': 'a yellow fruit', 'etymology': 'Arabic', 'synonyms': ['fruit'], 'antonyms': ['vegetable'], 'example': 'Bananas are rich in potassium.', 'mnemonic': 'Bananas are yellow like the sun.', 'is_completed':True},
    {'word': 'cherry', 'meaning': 'a small red fruit', 'etymology': 'Greek', 'synonyms': ['fruit', 'berry'], 'antonyms': ['vegetable'], 'example': 'Cherries are in season in summer.', 'mnemonic': 'Cherries are like small, sweet jewels.', 'is_completed':False},
    {'word': 'dog', 'meaning': 'a domesticated animal', 'etymology': 'Old English', 'synonyms': ['canine', 'puppy'], 'antonyms': ['cat'], 'example': 'My dog loves to play in the park.', 'mnemonic': 'Dogs are man’s best friend.', 'is_completed':False},
    {'word': 'elephant', 'meaning': 'a large mammal', 'etymology': 'Latin', 'synonyms': ['mammal', 'animal'], 'antonyms': ['mouse'], 'example': 'Elephants are known for their memory.', 'mnemonic': 'Elephants never forget.', 'is_completed':False},
    {'word': 'flower', 'meaning': 'a plant that blooms', 'etymology': 'Latin', 'synonyms': ['blossom', 'bloom'], 'antonyms': ['weed'], 'example': 'The garden is full of beautiful flowers.', 'mnemonic': 'Flowers are nature’s decoration.', 'is_completed':False},
    {'word': 'giraffe', 'meaning': 'a tall African animal with a long neck', 'etymology': 'Arabic', 'synonyms': ['animal', 'mammal'], 'antonyms': ['lion'], 'example': 'The giraffe grazes on leaves from tall trees.', 'mnemonic': 'Giraffes are giants with gentle necks.', 'is_completed':False},
    {'word': 'house', 'meaning': 'a place where people live', 'etymology': 'Old English', 'synonyms': ['home', 'dwelling'], 'antonyms': ['apartment'], 'example': 'They just bought a new house.', 'mnemonic': 'A house is a structure, a home is a feeling.', 'is_completed':False},
    {'word': 'ice', 'meaning': 'frozen water', 'etymology': 'Old English', 'synonyms': ['frost', 'glacier'], 'antonyms': ['water'], 'example': 'The ice in the drink melted quickly.', 'mnemonic': 'Ice is cold as stone.', 'is_completed':False},
    ]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/learning')
def learning():
    # 学習した単語の数（例として10を使用）
    learned_words_count = 160

    # 学習進捗に応じた励ましのメッセージを生成
    if learned_words_count < 50:
        encouragement_message = "最初の一歩は大切です！その調子でがんばりましょう！"
    elif learned_words_count < 200:
        encouragement_message = "順調です！少しずつ前進していますね！"
    else:
        encouragement_message = "素晴らしい進捗です！このまま続けてください！"

    return render_template('learning.html',
                            words=words,
                            learned_words_count=learned_words_count,
                            encouragement_message = encouragement_message
                            )

@app.route('/learning/<int:word_index>')
def learning_word(word_index):
    # 現在の単語を取得
    current_word = words[word_index]
    # 他人の例文のサンプルデータ
    other_examples = [
        {'text': 'This is a sample sentence from another user.', 'ai_rating': 'Good example'},
        {'text': 'Another example sentence for learning.', 'ai_rating': 'Needs improvement'}
    ]
    return render_template('learningword.html',
                           word_data=current_word,
                           other_examples=other_examples)

@app.route('/review')
def review():
    # サンプル単語データ
    words = [
        {'word': 'apple', 'meaning': 'リンゴ'},
        {'word': 'banana', 'meaning': 'バナナ'},
        {'word': 'cat', 'meaning': '猫'},
        {'word': 'dog', 'meaning': '犬'},
        {'word': 'elephant', 'meaning': '象'},
        {'word': 'flower', 'meaning': '花'},
        {'word': 'guitar', 'meaning': 'ギター'},
        {'word': 'house', 'meaning': '家'},
        {'word': 'island', 'meaning': '島'},
        {'word': 'jungle', 'meaning': 'ジャングル'},
        {'word': 'kangaroo', 'meaning': 'カンガルー'},
        {'word': 'lion', 'meaning': 'ライオン'},
        {'word': 'mountain', 'meaning': '山'},
        {'word': 'notebook', 'meaning': 'ノート'},
        {'word': 'orange', 'meaning': 'オレンジ'}
    ]
    # 学習済みの単語（例として勉強した単語数を追跡）
    reviewed_words = ['apple', 'banana']
    review_progress = len(reviewed_words)
    total_words = len(words)
    return render_template('review.html',
                           words=words,
                           review_progress=review_progress,
                           total_words=total_words)

if __name__ == '__main__':
    app.run(debug=True)
