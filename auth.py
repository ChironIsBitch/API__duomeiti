# -*- coding: utf-8 -*-

import time
import random
import hmac, hashlib
import binascii
import base64

AUTH_SECRET_ID_KEY_ERROR = -1

def gen_sign(appid, secret_key, expired):
    if not appid or not secret_key:
        return AUTH_SECRET_ID_KEY_ERROR

    expired = int(expired)
    now = int(time.time())
    rdm = random.randint(0, 999999999)
    plain_text = 'a=' + str(appid) + '&e=' + str(expired) + '&t=' + str(now) + '&r=' + str(rdm)
    bin = hmac.new(secret_key.encode(), plain_text.encode(), hashlib.sha1)
    s = bin.hexdigest()
    s = binascii.unhexlify(s)
    s = s + plain_text.encode('ascii')
    signature = base64.b64encode(s).rstrip()    #生成签名
    return signature
