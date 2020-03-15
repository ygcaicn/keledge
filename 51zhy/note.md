# [悦读](https://yd.51zhy.cn/)

fake js:

https://yd.51zhy.cn/ebook/reader/static/js/0.c076253798e5c0484c22.1584106987869.js

tool:

<https://coding.tools/cn/ascii-to-hex>

## 获取authorize

hook:output_authorize

https://bridge.51zhy.cn/transfer//content/authorize

浏览器initiator找到请求

关键词：SplitFileUrls

```
success -> \x73\x75\x63\x63\x65\x73\x73
Data -> \x44\x61\x74\x61
SplitFileUrls -> \x53\x70\x6c\x69\x74\x46\x69\x6c\x65\x55\x72\x6c\x73
```

```js
_0x5e81ba['\x61\x6a\x61\x78']({
                                '\x75\x72\x6c': _0x237e96['\x72\x65\x61\x64\x44\x61\x74\x61']['\x75\x72\x6c'],
                                '\x74\x69\x6d\x65\x6f\x75\x74': 0xea60,
                                '\x74\x79\x70\x65': '\x50\x4f\x53\x54',
                                '\x64\x61\x74\x61\x54\x79\x70\x65': '\x6a\x73\x6f\x6e',
                                '\x64\x61\x74\x61': _0x4fb6bf,
                                '\x73\x75\x63\x63\x65\x73\x73': function(_0x49fe70) {
                                    console['\x6c\x6f\x67'](_0x49fe70),
                                    _0x49fe70['\x53\x75\x63\x63\x65\x73\x73'] ? (_0x237e96['\x69\x6d\x70\x6f\x77\x65\x52\x65\x73'] = _0x49fe70['\x44\x61\x74\x61']['\x53\x70\x6c\x69\x74\x46\x69\x6c\x65\x55\x72\x6c\x73'],
                                    _0x237e96['\x41\x6c\x6c\x6f\x77\x52\x65\x61\x64\x50\x65\x72\x63\x65\x6e\x74\x61\x67\x65'] = _0x49fe70['\x44\x61\x74\x61']['\x41\x6c\x6c\x6f\x77\x52\x65\x61\x64\x50\x65\x72\x63\x65\x6e\x74\x61\x67\x65'] ? _0x49fe70['\x44\x61\x74\x61']['\x41\x6c\x6c\x6f\x77\x52\x65\x61\x64\x50\x65\x72\x63\x65\x6e\x74\x61\x67\x65'] : 0.2,
                                    _0x237e96['\x61\x75\x74\x68\x6f\x72\x4b\x65\x79'] = _0x237e96['\x6d\x61\x6b\x65\x4b\x65\x79'](_0x49fe70[a2_0xe4fb('\x30\x78\x32\x38\x32')]['\x4b\x65\x79']),
                                    _0x237e96['\x6e\x75\x6d\x62\x65\x72\x4f\x66\x50\x61\x67\x65\x73'] = _0x49fe70['\x44\x61\x74\x61']['\x53\x70\x6c\x69\x74\x46\x69\x6c\x65\x55\x72\x6c\x73']['\x6c\x65\x6e\x67\x74\x68'],
                                    _0x237e96['\x6d\x61\x72\x6b\x52\x65\x61\x64\x65\x64'](),
                                    _0x1c4460['\x72\x65\x73\x6f\x6c\x76\x65'](_0x49fe70)) : 0x22 === _0x49fe70['\x43\x6f\x64\x65'] && (location['\x68\x72\x65\x66'] = localStorage['\x65\x62\x6f\x6f\x6b\x6d\x61\x69\x6e\x68\x6f\x73\x74'] + '\x2f\x65\x62\x6f\x6f\x6b\x2f\x77\x65\x62\x2f\x6e\x65\x77\x42\x6f\x6f\x6b\x2f\x72\x65\x61\x64\x54\x72\x61\x6e\x73\x66\x65\x72\x3f\x69\x64\x3d' + _0x237e96['\x24\x72\x6f\x75\x74\x65']['\x71\x75\x65\x72\x79']['\x69\x64'] + '\x26\x72\x65\x61\x64\x54\x79\x70\x65\x3d\x70\x64\x66\x26\x61\x63\x74\x69\x6f\x6e\x54\x79\x70\x65\x3d\x6c\x6f\x67\x69\x6e');
                                },
                                '\x65\x72\x72\x6f\x72': function(_0x37aa48) {
                                    _0x237e96['\x24\x6d\x65\x73\x73\x61\x67\x65']['\x77\x61\x72\x6e\x69\x6e\x67'](_0x37aa48['\x44\x65\x73\x63\x72\x69\x70\x74\x69\x6f\x6e']),
                                    setTimeout(function() {
                                        window['\x63\x6c\x6f\x73\x65']();
                                    }, 0x1388);
                                },
                                '\x63\x6f\x6d\x70\x6c\x65\x74\x65': function(_0x3554d7, _0x357304) {
                                    '\x74\x69\x6d\x65\x6f\x75\x74' == _0x357304 && setTimeout(function() {
                                        window['\x63\x6c\x6f\x73\x65']();
                                    }, 0x1388);
                                }
                            })
```

```js
'use strict';
_0x5e81ba["ajax"]({
  "url" : _0x237e96["readData"]["url"],
  "timeout" : 6E4,
  "type" : "POST",
  "dataType" : "json",
  "data" : _0x4fb6bf,
  "success" : function(data) {
    console["log"](data);
    if (data["Success"]) {
      _0x237e96["impoweRes"] = data["Data"]["SplitFileUrls"];
      _0x237e96["AllowReadPercentage"] = data["Data"]["AllowReadPercentage"] ? data["Data"]["AllowReadPercentage"] : 0.2;
      _0x237e96["authorKey"] = _0x237e96["makeKey"](data[a2_0xe4fb("0x282")]["Key"]);
      _0x237e96["numberOfPages"] = data["Data"]["SplitFileUrls"]["length"];
      _0x237e96["markReaded"]();
      _0x1c4460["resolve"](data);
    } else {
      if (34 === data["Code"]) {
        /** @type {string} */
        location["href"] = localStorage["ebookmainhost"] + "/ebook/web/newBook/readTransfer?id=" + _0x237e96["$route"]["query"]["id"] + "&readType=pdf&actionType=login";
      }
    }
  },
  "error" : function(deleted_model) {
    _0x237e96["$message"]["warning"](deleted_model["Description"]);
    setTimeout(function() {
      window["close"]();
    }, 5E3);
  },
  "complete" : function(i, keyValuePairsObj) {
    if ("timeout" == keyValuePairsObj) {
      setTimeout(function() {
        window["close"]();
      }, 5E3);
    }
  }
});
```
## 获取passwd

hook:output_password

关键词：

```
CryptoJS
authorKey -> \x61\x75\x74\x68\x6f\x72\x4b\x65\x79
AES -> \x41\x45\x53
decrypt -> \x64\x65\x63\x72\x79\x70\x74
["Utf8"]["parse"] -> ["\x55\x74\x66\x38"]["\x70\x61\x72\x73\x65"]
```

## 注意

必须加载jquery，否则layer会出错

loadJs("https://cdn.bootcss.com/jquery/3.4.1/jquery.min.js")
