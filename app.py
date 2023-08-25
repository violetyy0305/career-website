from flask import Flask
#import class Flask from flask

app = Flask(__name__)


@app.route("/")
def hello_world():
  return "Hello, World!"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  # host=localhost