import random
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/test')
def test():
    number = random.randint(1, 10)
    print(number)

    return f'number : {number}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)

    