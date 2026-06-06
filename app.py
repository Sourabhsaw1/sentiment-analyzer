from flask import Flask, render_template, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text', '')
    
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    
    if polarity > 0:
        sentiment = 'Positive 😊'
    elif polarity < 0:
        sentiment = 'Negative 😞'
    else:
        sentiment = 'Neutral 😐'
    
    return jsonify({
        'sentiment': sentiment,
        'polarity': round(polarity, 2),
        'subjectivity': round(subjectivity, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)