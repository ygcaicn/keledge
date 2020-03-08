#!/usr/bin/env python3
import requests
import json
import os
import argparse
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed

from utils import dowloadSplitFileUrl, decSplitFile
FORMAT = '%(levelname)-4s: %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
def dowloadSplitFiles(SplitFiles):
    enc_dir = os.path.join(base_dir, book_prefix+'_enc')
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = {executor.submit(dowloadSplitFileUrl, enc_dir, obj): obj for obj in SplitFiles}
        for future in as_completed(future_to_url):
            obj = future_to_url[future]
            try:
                ret = future.result()
            except Exception as exc:
                logging.warning('%r generated an exception: %s' % (obj, exc))
            else:
                logging.info(ret)

def dowloadSplitFilesByLoop(SplitFiles):
    enc_dir = os.path.join(base_dir, book_prefix+'_enc')
    for obj in SplitFiles:
        ret = dowloadSplitFileUrl(enc_dir,  obj)
        logging.info(ret)

def decSplitFiles(enc_dir, dec_dir):
    ok = 0
    with ThreadPoolExecutor(max_workers=16) as executor:
        for root,_,files in os.walk(enc_dir):
            future_to_url = {executor.submit(decSplitFile, passwd, os.path.join(root,f), os.path.join(dec_dir, f)): f for f in files}
        for future in as_completed(future_to_url):
            obj = future_to_url[future]
            try:
                ret = future.result()
            except Exception as exc:
                logging.warning('%r generated an exception: %s' % (obj, exc))
            else:
                if ret == None:
                    ok+=1
                    logging.info("alerady decrypt.")
                elif ret.returncode == 0:
                    ok+=1
                    logging.info("decrypt ok. {}".format(ret.stdout.decode()))
                else:
                    logging.error(ret.stderr.decode())
    print("总共：{}页\n成功：{}页".format(result['Data']['NumberOfPages'],ok))
    return ok



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', dest='authorize_file', required=True, action='store',
                    help='authorize file')
    parser.add_argument('-p', dest='passwd_file', action='store',
                    help='passwd file')
    args = parser.parse_args()
    authorize_file = args.authorize_file
    base_dir = os.path.dirname(authorize_file)
    book_prefix = os.path.basename(authorize_file).replace('_authorize.txt','')
    if args.passwd_file is None:
        passwd_file = os.path.join(base_dir, book_prefix+"_passwd.txt")
        if not os.path.exists(passwd_file):
            logging.warning("[未找到passwd文件，请使用-p指定]")
            parser.print_help()
            exit(1)

    with open(authorize_file) as authorize:
        result = json.load(authorize)
    with open(passwd_file, 'rt') as pwd:
        passwd = pwd.read(1024)

    SplitFiles = result['Data']['SplitFiles']

    while True:
        dowloadSplitFiles(SplitFiles)
        # dowloadSplitFilesByLoop(SplitFiles)
        enc_dir = os.path.join(base_dir, book_prefix+'_enc')
        dec_dir = os.path.join(base_dir, book_prefix+'_dec')
        ok = decSplitFiles(enc_dir, dec_dir)
        if ok < result['Data']['NumberOfPages']:
            retry = input("再次尝试？[Y/n]")
            if retry not in ['N', 'n', 'Not', 'not']:
                continue
            else:
                break
        else:
            break
