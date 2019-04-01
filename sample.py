# -*- coding: utf-8 -*-

import time
import auth
import requests
import json

appid = '16448'
secret_key =  'gfehWKydKGhaZKNv45fjbRNALM4'

if __name__ == '__main__':
    auth_key = str(auth.gen_sign(appid, secret_key, time.time()+3600), encoding='utf-8')


    data = {
        'base': {
            'appid': appid,
            'auth_key': auth_key,
            'cmds': ['NlpTts']
            },
        'params': {
            'mode': 'Daji',
        },
        'media': '梦想还是要有的,万一实现了呢',

    }

    rsp = requests.post('http://openai.qq.com/api/json/ai/GetMultiAI', json=data)
    print(rsp.text)
    print(type(rsp.text))
    shuju = json.loads(rsp.text)
    print(shuju)
    print(shuju['cmd_rsps']['NlpTts']['data']['voice_url'])


