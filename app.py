import flask
from flask import request
from model import predict_sentiment
import os
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)

response = {}
@app.route('/predict', methods=["GET","POST"])
def index():
    if request.method =="POST":
        text_input = request.form["text_input"]
    else:
        text_input = request.args.get('text_input')


        # Passes contents of query string to the prediction function contained in model.py
    prediction = predict_sentiment(text_input)
    print(prediction[0]['prob'])

        # Indexes the returned dictionary for the sentiment probability
    if((prediction[0]['prob']) > 0.5):
        prediction = "1"
        
    else:
        prediction = "0"
    return flask.jsonify({'result': prediction})




if __name__ == '__main__':
    app.run(port=3000, debug=True)
