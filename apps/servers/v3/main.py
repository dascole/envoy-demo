from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/service1')
def svc1():
    return ("<body style='background:#b2c0f7; font-size:20px'>SERVER 3: /SERVICE1 route</body>")

@app.route('/')
def main():
    homer = """
   ___  _____    
 .'/,-Y"     "~-.  
 l.Y             ^.           
 /\               _\_      "Doh!!"   
i            ___/"   "\ 
|          /"   "\   o !   
l         ]     o !__./   
 \ _  _    \.___./    "~\  
  X \/ \            ___./  
 ( \ ___.   _..--~~"   ~`-.  
  ` Z,--   /               \    
    \__.  (   /       ______) 
      \   l  /-----~~" /      
       Y   \          / 
       |    "x______.^ 
       |           \    
       j            Y
    """
    return ("<body style='background:#b2c0f7; font-size:20px'><pre>" + homer + "</pre></body>")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7773, debug=True)
