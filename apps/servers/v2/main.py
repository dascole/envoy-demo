from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/service1')
def svc1():
    return ("<body style='background:#b2c0f7; font-size:20px'>SERVER 2: /SERVICE1 route</body>")

@app.route('/')
def main():
    keg = """
                    /
                   |
                .-/',;\-.
                |'\\;;;\'
                |:| \;'
                |'|
                |:|
    ____________|'|______
  |'.           |:|      '.
  |  '. ___________________'.
  |    |.-------------------.._
  |    ||       |'|         || `--._
  |    || _..--'|:|'--.._   ||      `-._
  |    |||'--..____..--'|   |[]        ||
  |    |||              |   ||         ||
  |    |||              |   ||         ||
  |    ||]'--..____..--'[   ||         ||
  |    |||              |   ||         ||
  |    |L|              |   ||         ||
  |    |||              |   ||         J|
  |    ||]'--..____..--'[   ||         ||
  |    |||              |   ||         ||
  |    |||              |.  |[]        ||
  |    ||'--..______..--' '.||         ||
  |    |'-------------------'|         ||
   '.  | Beer Box ||..___..||`--._     ||
     '.|____________________|     `--._||
    """
    return ("<body style='background:#b2c0f7; font-size:20px'><pre>" + keg + "</pre></body>")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7772, debug=True)
