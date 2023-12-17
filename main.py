from flask import Flask, request, jsonify
from Exceptions import CalcError
from Polish import evaluate

app = Flask(__name__)


@app.route('/api/calculator', methods=['POST'])
def add_new_equation():
    expression = request.json['expression']
    try:
        res = evaluate(expression)
        return jsonify({'answer': res})
    except CalcError as e:
        return jsonify({'error': str(e)})


if __name__ == "__main__":
    app.run(port=3000, host="localhost")
    # example0 = "1 + 1"
    # example1 = "( 1 + 1 + 2 + 2 ) * 2 * 3"
    # example2 = "( -1 + -1 + -2 + -2 ) * -2 * -3"
    # example3 = "( 1.5 + 1.98 + 2.45 + 2.76 ) * 2.564646 * -3.6546468486"
