import joblib
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Load the dataset
data = pd.read_csv('shuffled_dataset.csv')

# Split the data into input features (X) and labels (y)
X = data['WORD']
y = data['LABEL']

# Vectorize the input features
vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)

# Train the logistic regression model
model = LogisticRegression()
model.fit(X_vec, y)
joblib.dump(model, 'trained_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')
# Classify user input
user_input = input("Enter a word: ")
user_input_vec = vectorizer.transform([user_input])
prediction = model.predict(user_input_vec)
print("Prediction:", prediction)