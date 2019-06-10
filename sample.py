# -*- coding: utf-8 -*-

import time
import auth
import requests
import json




appid = '16448'
secret_key =  'gfehWKydKGhaZKNv45fjbRNALM4'

if __name__ == '__main__':
    auth_key = str(auth.gen_sign(appid, secret_key, time.time()+3600), encoding='utf-8')
    while 1:
        qq = input()
        data = {
            'base': {
                'appid': appid,
                'auth_key': auth_key,
                'cmds': ['NlpTts'],
                'speed' :'faster',
                },
            'media':qq,
            "params": {
                    "NlpTts": {
                            "mode": "Daji",
                            "speed":"normal",
                            
                    }
            },


        }

        rsp = requests.post('http://openai.qq.com/api/json/ai/GetMultiAI', json=data)
        shuju = json.loads(rsp.text)
        print(shuju['cmd_rsps']['NlpTts']['data']['voice_url'])


