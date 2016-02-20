import hashlib
from flask import (Flask, request)
from wechat_sdk import WechatBasic
from config import conf
#from wechat_sdk.exceptions import ParseError

wechat = WechatBasic(conf=conf)

app = Flask(__name__)


@app.route('/hello/')
def dispatcher():
    signature = request.args.get('signature')
    timestamp = request.args.get('timestamp')
    nonce = request.args.get('nonce')
    echostr = request.args.get('echostr')
    list = [conf.token, timestamp, nonce]
    list.sort()
    sha1 = hashlib.sha1()
    map(sha1.update, list)
    hashcode = sha1.hexdigest()
    if wechat.check_signature(signature, timestamp, nonce):
        if signature == hashcode:
            return echostr
    else:
        return 'Wrong Client'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
