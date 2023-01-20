import time
import vmessDESlib
from pyDes import des, CBC, PAD_PKCS5
from flask import *

realServerIP = '请填入服务地址'

with open('keyfile.key', 'r') as f:
    key = f.read()

app = Flask('vmess-plus-httpserver-auth')
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/authme/api/')
def login():
    password = 'getServerInfo'
    userSendPassword = vmessDESlib.des_descrypt(request.args.set('key'),key)
    if(str(userSendPassword) == password):
        command = vmessDESlib.des_encrypt(realServerIP,key)
        return jsonify({'status':'success','username':command})
    else:
        return jsonify({'status':'success','username':request.args.get('username')})


if __name__ == '__main__':
    print('vmess-plus-httpserver-auth starting...')
    app.run(host='0.0.0.0',port=5097,debug=True)
    