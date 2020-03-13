#!/usr/bin/env python3
import os
import time
import random
import json
import requests
import subprocess
from datetime import datetime

h = '''
Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache
Accept: application/json, text/plain, */*
Sec-Fetch-Dest: document
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Referer: https://www.keledge.com
Accept-Encoding: gzip, deflate, br
Accept-Language: en,zh-CN;q=0.9,zh;q=0.8,pt;q=0.7

'''

headers = dict([i.split(': ', 1) for i in h.split('\n') if i != ''])
headers = {}
def dowloadSplitFileUrl(d, obj, t=0, overwrite=0, ):
    
    if not os.path.exists(d):
        os.makedirs(d)
    
    page = obj['NumberOfPage']
    name = os.path.join(d, "{}.pdf".format(page))
    if os.path.exists(name) and os.path.getsize(name) < 2000:
        os.remove(name)
    if os.path.exists(name) and overwrite==0:
        return "已存在！{}".format(name)
        

    url = obj['Url']
    r = requests.get(url, headers=headers)
    if r.status_code >= 300:
        time.sleep(max(5, t))

        return "下载失败：{} {}".format(name, r.status_code)
    if len(r.content) < 2000:
        try:
            r.content.decode()
        except UnicodeDecodeError:
            # 空白页
            with open(name, 'wb') as f:
                f.write(r.content)
            return "下载成功！空白页{} http_status:{}".format(name, r.status_code)
        time.sleep(max(30, t))
        return "下载失败：{} {} {} size:{}Bytes\n{}".format(name, r.status_code, url, len(r.content), r.text)
    with open(name, 'wb') as f:
        f.write(r.content)

    time.sleep(max(random.randint(10,20), t))
    return "下载成功！{} http_status:{}".format(name, r.status_code)

def decSplitFile(p, i, o):
    d = os.path.dirname(o)
    if not os.path.exists(d):
        os.makedirs(d)

    if os.path.exists(o):
        return
    cmd = 'openssl enc -d -aes-128-ecb -K "{}" -in "{}" -out "{}"'.format(p, i, o)
    
    # cmd = cmd.split()
    r = subprocess.run(cmd, capture_output=True, shell=True)
    if r.returncode != 0:
        if os.path.exists(o):
            os.remove(o)
    return r
