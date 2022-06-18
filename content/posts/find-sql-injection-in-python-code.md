---
title: "Find SQL injection in Python code"
date: 2017-12-11T10:08:06+08:00
enableDisqus: true
Categories:
  - coding
Tags:
  - Python
---

[https://github.com/uber/py-find-injection](https://github.com/uber/py-find-injection)

用程式化的方式掃出 code base 沒有乖乖用 paramstyle sql 語句

![Imgur](https://i.imgur.com/P18DyHR.jpg)

<!--more-->

鴿子封包，uber 在 2013 年丟出來的玩具

原理利用 AST 拆 code 找出特定的 function name，並比對第一個參數有沒有用過字串串接

[default 會找 session.execute cursor.execute](https://github.com/uber/py-find-injection/blob/f91c137e8b78424bec78085df771b1a6f62c6769/py_find_injection/__init__.py#L80)

簡單但有效，clone 下來改也很快。

其中找[字串串接的 code](https://github.com/uber/py-find-injection/blob/master/py_find_injection/__init__.py#L62)也滿有趣的，值得一讀


但是歹記通常不是憨人想得這麼簡單，code base 裡面總有為了省事，及不好處理的 list parameter，
而自己串 sql。有年紀的 codebase 掃下去大概只有淚與累，大概只能用在自己開發或是放在 CI 上逼死同事。
