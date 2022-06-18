---
title: "Pip 藏有惡意套件"
date: 2017-09-25T08:20:05+08:00
enableDisqus: true
Categories:
  - coding
Tags:
  - Python
---

有一段時間了 20170909 的報告
[http://www.nbu.gov.sk/skcsirt-sa-20170909-pypi/](http://www.nbu.gov.sk/skcsirt-sa-20170909-pypi/)

<!--more-->

某組織發出的研究報告，指出 pip 裡面有若干 package 用很像的名字進行偽裝

譬如說 `crypto` -> `crypt`

偽裝的 package 會在 setup.py 裡面加料，system admin 只要 pip install 就會直接中招

可以用這個檢查，檢查如果有直接移除重裝即可
```bash
pip list --format=legacy | egrep '^(acqusition|apidev-coop|bzip|crypt|django-server|pwd|setup-tools|telnet|urlib3|urllib) '
```

[stackoverflow](https://stackoverflow.com/questions/44351366/python-3-unable-to-install-crypt-module-successfully) 也有撿到以前的受害者 lol


值得一提的是，惡意程式碼只會把一些系統資訊傳回在中國的 ip，並加上了這段註解，略佛？
```python
# Welcome Here! :)
# just toy, no harm :)
```
