from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/service1')
def svc1():
    return ("<body style='background:#b2c0f7; font-size:20px'>SERVER 1: /SERVICE1 route</body>")

@app.route('/')
def main():
    bond = """
       ________   ________    _________  ____________;_
      - ______ \ - ______ \ / _____   //.  .  ._______/
     / /     / // /     / //_/     / // ___   /
    / /     / // /     / /       .-'//_/|_/,-'
   / /     / // /     / /     .-'.-'
  / /     / // /     / /     / /
 / /     / // /     / /     / /
/ /_____/ // /_____/ /     / /
\________- \________-     /_/
"""
    return ("<body style='background:#b2c0f7; font-size:20px'><pre>" + bond + "</pre></body>")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7771, debug=True)
