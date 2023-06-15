import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def extract_keywords(text):
    # Tokenize the text into words
    tokens = word_tokenize(text)

    # Get the list of English stopwords
    stop_words = set(stopwords.words('english'))

    # Filter out stopwords and punctuation marks
    keywords = [word for word in tokens if word.lower() not in stop_words and word.isalpha()]

    return keywords

# Example usage
input_text = "Center a div both horizontally and vertically with CSS"
keywords = extract_keywords(input_text)
print(keywords)