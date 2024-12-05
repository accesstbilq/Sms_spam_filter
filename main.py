# from flask import Flask, render_template, request
# import joblib
# import pandas as pd
# import re   
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# from nltk.stem import PorterStemmer

# app = Flask(__name__)

# model = joblib.load('spam_classifier_model.joblib')
# vectorizer = joblib.load('spam_vectorizer.joblib')

contractions = { 
"ain't": "am not / are not / is not / has not / have not",
"aren't": "are not / am not",
"can't": "cannot",
"can't've": "cannot have",
"'cause": "because",
"could've": "could have",
"couldn't": "could not",
"couldn't've": "could not have",
"didn't": "did not",
"doesn't": "does not",
"don't": "do not",
"hadn't": "had not",
"hadn't've": "had not have",
"hasn't": "has not",
"haven't": "have not",
"he'd": "he had / he would",
"he'd've": "he would have",
"he'll": "he shall / he will",
"he'll've": "he shall have / he will have",
"he's": "he has / he is",
"how'd": "how did",
"how'd'y": "how do you",
"how'll": "how will",
"how's": "how has / how is / how does",
"I'd": "I had / I would",
"I'd've": "I would have",
"I'll": "I shall / I will",
"I'll've": "I shall have / I will have",
"I'm": "I am",
"I've": "I have",
"isn't": "is not",
"it'd": "it had / it would",
"it'd've": "it would have",
"it'll": "it shall / it will",
"it'll've": "it shall have / it will have",
"it's": "it has / it is",
"let's": "let us",
"ma'am": "madam",
"mayn't": "may not",
"might've": "might have",
"mightn't": "might not",
"mightn't've": "might not have",
"must've": "must have",
"mustn't": "must not",
"mustn't've": "must not have",
"needn't": "need not",
"needn't've": "need not have",
"o'clock": "of the clock",
"oughtn't": "ought not",
"oughtn't've": "ought not have",
"shan't": "shall not",
"sha'n't": "shall not",
"shan't've": "shall not have",
"she'd": "she had / she would",
"she'd've": "she would have",
"she'll": "she shall / she will",
"she'll've": "she shall have / she will have",
"she's": "she has / she is",
"should've": "should have",
"shouldn't": "should not",
"shouldn't've": "should not have",
"so've": "so have",
"so's": "so as / so is",
"that'd": "that would / that had",
"that'd've": "that would have",
"that's": "that has / that is",
"there'd": "there had / there would",
"there'd've": "there would have",
"there's": "there has / there is",
"they'd": "they had / they would",
"they'd've": "they would have",
"they'll": "they shall / they will",
"they'll've": "they shall have / they will have",
"they're": "they are",
"they've": "they have",
"to've": "to have",
"wasn't": "was not",
"we'd": "we had / we would",
"we'd've": "we would have",
"we'll": "we will",
"we'll've": "we will have",
"we're": "we are",
"we've": "we have",
"weren't": "were not",
"what'll": "what shall / what will",
"what'll've": "what shall have / what will have",
"what're": "what are",
"what's": "what has / what is",
"what've": "what have",
"when's": "when has / when is",
"when've": "when have",
"where'd": "where did",
"where's": "where has / where is",
"where've": "where have",
"who'll": "who shall / who will",
"who'll've": "who shall have / who will have",
"who's": "who has / who is",
"who've": "who have",
"why's": "why has / why is",
"why've": "why have",
"will've": "will have",
"won't": "will not",
"won't've": "will not have",
"would've": "would have",
"wouldn't": "would not",
"wouldn't've": "would not have",
"y'all": "you all",
"y'all'd": "you all would",
"y'all'd've": "you all would have",
"y'all're": "you all are",
"y'all've": "you all have",
"you'd": "you had / you would",
"you'd've": "you would have",
"you'll": "you shall / you will",
"you'll've": "you shall have / you will have",
"you're": "you are",
"you've": "you have"
}

# def predict_spam(text, contractions):
#     text = text.lower()
    
#     for contraction, expansion in contractions.items():
#         text = re.sub(r'\b' + re.escape(contraction) + r'\b', expansion, text, flags=re.IGNORECASE)
    
#     text = re.sub(r'[^\w\s]', '', text)
    
#     tokens = word_tokenize(text.lower())
#     english_stopwords = set(stopwords.words('english'))
#     tokens_wo_stopwords = [word for word in tokens if word not in english_stopwords]
#     text = ' '.join(tokens_wo_stopwords)
    
#     ps = PorterStemmer()
#     words = text.lower().split()
#     stemmed_words = [ps.stem(word) for word in words]
#     text = ' '.join(stemmed_words)
    
#     num_words = len(word_tokenize(text))
    
#     bow_matrix = vectorizer.transform([text])
    
#     input_features = pd.DataFrame(bow_matrix.toarray())
#     input_features['num_words'] = num_words
#     input_features = input_features.rename(str, axis="columns")
    
#     prediction = model.predict(input_features)
    
#     return "Spam" if prediction[0] == 1 else "Not Spam"

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     prediction = None
#     input_text = ''
    
#     if request.method == 'POST':
#         input_text = request.form['text']
#         prediction = predict_spam(input_text, contractions)
    
#     return render_template('index.html', prediction=prediction, input_text=input_text)

# if __name__ == '__main__':
#     app.run(debug=False, host='0.0.0.0', port=7878)



from flask import Flask, render_template, request
import joblib
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

app = Flask(__name__)

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

models = {
    'Gradient Boosting': joblib.load('gb_model.joblib'),
    'K-Nearest Neighbors': joblib.load('knn_model.joblib'),
    'Random Forest': joblib.load('rf_model.joblib')
}

vectorizer = joblib.load('spam_vectorizer.joblib')

def preprocess_text(text, contractions):
    text = text.lower()

    for contraction, expansion in contractions.items():
        text = re.sub(r'\b' + re.escape(contraction) + r'\b', expansion, text, flags=re.IGNORECASE)
    
    text = re.sub(r'[^\w\s]', '', text)
    
    tokens = word_tokenize(text.lower())
    english_stopwords = set(stopwords.words('english'))
    tokens_wo_stopwords = [word for word in tokens if word not in english_stopwords]
    text = ' '.join(tokens_wo_stopwords)
    
    ps = PorterStemmer()
    words = text.lower().split()
    stemmed_words = [ps.stem(word) for word in words]
    text = ' '.join(stemmed_words)
    
    return text

def predict_spam(text, model_name):
    processed_text = preprocess_text(text, contractions)
    
    num_words = len(word_tokenize(processed_text))
    
    bow_matrix = vectorizer.transform([processed_text])
    
    input_features = pd.DataFrame(bow_matrix.toarray())
    input_features['num_words'] = num_words
    input_features = input_features.rename(str, axis="columns")
    
    model = models[model_name]
    
    prediction = model.predict(input_features)
    
    return "Spam" if prediction[0] == 1 else "Not Spam"

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    input_text = ''
    selected_model = 'Gradient Boosting'
    
    if request.method == 'POST':
        input_text = request.form['text']
        selected_model = request.form.get('model', 'Gradient Boosting')
        prediction = predict_spam(input_text, selected_model)
    
    return render_template('index.html', 
                           prediction=prediction, 
                           input_text=input_text, 
                           models=list(models.keys()),
                           selected_model=selected_model)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=7878)