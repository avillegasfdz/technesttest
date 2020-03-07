import requests

from flask import Flask, request, abort, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/process", methods=['POST'])
def process():
    """ Offers the process service for the POST method. """
    if request.method == "POST":
        try:
            number1 = int(request.form["number1"])
            number2 = int(request.form["number2"])
        except ValueError as exception:
            abort(400, "process must be called with two integers")

    url = 'http://localhost:55002/oddsum'

    data = {'number1': number1, 'number2': number2}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        return response.text
    else:
        abort(400, "Bad response from oddsum: " + response.text)
