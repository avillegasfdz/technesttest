from flask import Flask, request, abort

from oddsum import OddSum, OddException

app = Flask(__name__)


@app.route("/oddsum", methods=['POST'])
def oddsum():
    """ Offers the oddsum service for the POST method. """
    if request.method == "POST":
        number1 = request.form["number1"]
        number2 = request.form["number2"]
        try:
            return str(OddSum.sum(int(number1), int(number2)))
        except OddException as exception:
            return str(exception), 400
        except ValueError as exception:
            return "oddsum must be called with two integers", 400
