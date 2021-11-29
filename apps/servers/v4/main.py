from flask import Flask
from flask import request


app = Flask(__name__)

@app.route('/service1')
def svc1():
    return ("<body style='background:#b2c0f7; font-size:20px'>SERVER 4: /SERVICE1 route</body>")

@app.route('/')
def main():
    coffee = """
                        (
                          )     (
                   ___...(-------)-....___
               .-""       )    (          ""-.
         .-'``'|-._             )         _.-|
        /  .--.|   `""---...........---""`   |
       /  /    |                             |
       |  |    |                             |
        \  \   |                             |
         `\ `\ |                             |
           `\ `|                             |
           _/ /\                             /
          (__/  \                           /
       _..---""` \                         /`""---.._
    .-'           \                       /          '-.
   :               `-.__             __.-'              :
   :                  ) ""---...---"" (                 :
    '._               `"--...___...--"`              _.'
      \""--..__                              __..--""/
       '._     '''----.....______.....----'''     _.'
          `""--..,,_____            _____,,..--""`
                        `'''----'''`

    """
    return ("<body style='background:#b2c0f7; font-size:20px'><pre>" + coffee + "</pre></body>")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7774, debug=True)
