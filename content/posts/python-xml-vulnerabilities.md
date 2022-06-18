+++
date = "2017-03-13T18:00:32+08:00"
title = "python xml vulnerabilities"
image = "meme/xml.jpg"
categories = [
    "coding"
]
tags = [
    "Python",
    "xml"
]
+++

> It's just XML, what could probably go wrong? - Christian Heimes

<!--more-->

And ...

> XML is crap. Really. There are no excuses. XML is nasty to parse for humans, and it's a disaster to parse even for computers. There's just no reason for that horrible crap to exist. - Linus Trovalds

# Issue
最近 review 公司的一些外部服務的 callback api 的安全性。

其中一個 api 交換資訊使用 xml 格式傳送，而 parse 時用 Python standard library 的 xml module

[而 xml module 有一些安全性上的弱點](https://docs.python.org/2/library/xml.html#xml-vulnerabilities)

用 [wiki 的 billion laughs](https://en.wikipedia.org/wiki/Billion_laughs) sample code 當 payload 測試果然掛了，

充滿惡意的憤青們可以只用一台電腦癱瘓掉家裡所有 web node，

不過因為有鎖 ip ，所以也不是一個嚴重的安全性問題，廠廠。


# Solutions

看到問題後第一想法是不要用 xml module 處理，改用 lxml 之類的 3rd party lib

後來想想這問題應該滿普遍的，應該會有其他解法可以考慮。

期望可以有 Monkey Patch 或是至少提供相同 API 讓 migration 變得容易

問 Google 老師找到 [defusedxml](https://github.com/tiran/defusedxml) 專案看起來有八成七像

提供了相同 API，在 xmlrpc 部分是用 monkey patch，可以無痛轉換。


# Case closed
基本上在一個後 json 時代講 xml 實用性實在不高，不過人在江湖走跳，

難免介接利用其他第三方服務，尤其是銀行業仍偏好使用 xml，

在 parse 的時候還是需要注意是否會產生類似安全性問題。

Bomb has benn defused, counter terrorists win!

___btw 找不到開頭引言的來源，所以確實 Python developer 曾經講過這句話，然後在 repo 被公開處刑？___
