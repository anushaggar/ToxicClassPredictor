from flask import Flask,render_template,request
from flask_cors import cross_origin

#import tensorflow as tf
import joblib

app = Flask(__name__, template_folder="template")
model = joblib.load("./models/modell.pkl")
print("Model Loaded")


@app.route("/",methods=['GET'])
@cross_origin()
def home():
	return render_template("index.html")

@app.route("/predict",methods=['GET', 'POST'])
@cross_origin()
def predict():
	if request.method == "POST":		
		comment = str(request.form['comment'])
		print(comment)	
		pred = model.predict([comment])[0][0]
        
		if pred == 0:
			return render_template("negative.html")
		else:
			return render_template("positive.html")
	return render_template("index.html")


if __name__=='__main__':
	app.run(debug=True)

