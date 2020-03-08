# Keledge Pdf下载

3.478xxx.js
原始js，地址<https://cdn.keledge.com/web/static/js/3.47824973d763f5ca60a4.1583439609949.js>

nice.js
<http://www.jsnice.org/>
无法直接使用，可以用来与nice2.js对比分析逻辑。

nice2.js
实际overwirte使用的js。

## 密钥与解密

```js
case 7:
    return codeGeneratorFunc = node["sent"], ast = CryptoJS["enc"]["Utf8"]["parse"](this["v"]["authorKey"]), generatedCode = CryptoJS["AES"]["decrypt"](codeGeneratorFunc, ast, {
        "mode": CryptoJS["mode"]["ECB"],
        "padding": CryptoJS["pad"]["Pkcs7"]
    }), node["next"] = 12, this["wordArrayToU8"](generatedCode, flightPhase, refresh);
```

在nice2.js中

```js
case 0x7:return _0x322189=_0x2d73dd['\x73\x65\x6e\x74'],_0x3ae007=CryptoJS['\x65\x6e\x63']['\x55\x74\x66\x38']['\x70\x61\x72\x73\x65'](this['\x76']['\x61\x75\x74\x68\x6f\x72\x4b\x65\x79']),_0x10fe46=CryptoJS['\x41\x45\x53']['\x64\x65\x63\x72\x79\x70\x74'](_0x322189,_0x3ae007,{'\x6d\x6f\x64\x65':CryptoJS['\x6d\x6f\x64\x65']['\x45\x43\x42'],'\x70\x61\x64\x64\x69\x6e\x67':CryptoJS['\x70\x61\x64']['\x50\x6b\x63\x73\x37']}),_0x2d73dd['\x6e\x65\x78\x74']=0xc,this['\x77\x6f\x72\x64\x41\x72\x72\x61\x79\x54\x6f\x55\x38'](_0x10fe46,_0xe8aca2,_0x1a2353);
```

插入Hook之后：

```js
case 0x7:var ast=CryptoJS['\x65\x6e\x63']['\x55\x74\x66\x38']['\x70\x61\x72\x73\x65'](this['\x76']['\x61\x75\x74\x68\x6f\x72\x4b\x65\x79']);output_password(ast);return _0x322189=_0x2d73dd['\x73\x65\x6e\x74'],_0x3ae007=CryptoJS['\x65\x6e\x63']['\x55\x74\x66\x38']['\x70\x61\x72\x73\x65'](this['\x76']['\x61\x75\x74\x68\x6f\x72\x4b\x65\x79']),_0x10fe46=CryptoJS['\x41\x45\x53']['\x64\x65\x63\x72\x79\x70\x74'](_0x322189,_0x3ae007,{'\x6d\x6f\x64\x65':CryptoJS['\x6d\x6f\x64\x65']['\x45\x43\x42'],'\x70\x61\x64\x64\x69\x6e\x67':CryptoJS['\x70\x61\x64']['\x50\x6b\x63\x73\x37']}),_0x2d73dd['\x6e\x65\x78\x74']=0xc,this['\x77\x6f\x72\x64\x41\x72\x72\x61\x79\x54\x6f\x55\x38'](_0x10fe46,_0xe8aca2,_0x1a2353);
```

openssl enc -d -aes-128-ecb -K 406c322141214d6e4e446e505450386c -in enc.pdf -out dec.pdf
