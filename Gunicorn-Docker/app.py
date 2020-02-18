from flask import Flask
import os

app = Flask(__name__)

cf_port = os.getenv("PORT")


@app.route('/',methods=['POST'])
def hello_whale():
    return "This is the POST method of myapp"

@app.route('/',methods=['GET'])
def helo():
    return "This is the GET method of myapp"


if __name__ == '__main__':
	if cf_port is None:
		app.run(host='0.0.0.0', port=5000, debug=False)
	else:
		app.run(host='0.0.0.0', port=int(cf_port), debug=False)