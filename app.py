from flask import Flask, make_response

app = Flask(__name__)


@app.route('/health-check')
def index():
    response = make_response("This is a response with a 200 status code")
    response.status_code = 200
    return response


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
