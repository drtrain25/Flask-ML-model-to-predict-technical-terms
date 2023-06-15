# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
from flask import Flask, render_template, request, url_for, flash, redirect
from keyword_extractor import extract_keywords
import joblib

model = joblib.load('trained_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')
# from sklearn.linear_model import LogisticRegression

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

def predict_label(word):
    word_vec = vectorizer.transform([word])
    prediction = model.predict(word_vec)
    return prediction[0]

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
# @app.route('/')
# # ‘/’ URL is bound with hello_world() function.
# def hello_world():
# 	return 'Hello World'

# @app.route('/predictContext/<str>', methods=['GET','POST'])
# # ‘/’ URL is bound with hello_world() function.
# def hello_world(str):
# 	if request.method=="GET":
# 		words=extract_keywords(str)
# 		for i in words:
# 			prediction=classify_word(i,model)
# 			print(prediction,type(prediction))
# 		return "Hello World"
	
@app.route('/', methods=['POST'])
def classify_text():
    data = request.args.get("data")   # Get the request data as string
    words=extract_keywords(data) 
    print(words)
    print(data) # Convert the string into a list of words
    technical_count = 0
    for word in words:
        prediction = predict_label(word)
        print(prediction)
        if prediction == 1:
            print(word)
            technical_count += 1

    if (technical_count)>=2 or (technical_count/len(words))>=0.5:
        result = 'technical'
    else:
        result = 'non-technical'

    return result

# main driver function
if __name__ == '__main__':
	model = joblib.load('trained_model.pkl')
	vectorizer = joblib.load('vectorizer.pkl')

	# run() method of Flask class runs the application
	# on the local development server.
	app.run(port=4000, debug=True)