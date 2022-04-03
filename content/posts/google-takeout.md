---
title: "根據標籤下載 gmail 備份"
date: 2017-09-24T20:08:08+08:00
Categories:
  - coding
Tags:
  - Python
---

最近剛好有一些處理 email 資料的需求，要從一堆 exception mail 裡面撈出一些 id。

<!--more-->

之前數量不多都馬手動複製

但這次有幾十個 conversations 看了就很懶，我內心特爛軟

來問問看 Google 老師看有沒有聰明方法可以搞定這件事

...

\\[Google takeout](https://takeout.google.com/settings/takeout)/ 小叮噹語氣

本質上是 Google service 眾的備份工具，在備份 gmail 部分裡面，可以只下載特定 email label

還有一個問題是下載格式會是 mbox format，必須再做處理

流程會是這樣子的

- 把要 exported 的 email conversations 加一個新 label e.g. `exported`
- 去 Google takeout 請求該 label 的 backup
- Parse mbox file

![Imgur](https://i.imgur.com/ktWAnpW.png)


也找到有志同道合兄弟寫的 [Sydius/mbox-to-txt](https://github.com/Sydius/mbox-to-txt)

但這位 S 弟兄可能只要純文字，所以不吃的格式特多，這次要的資料被碼成 base64

參考一下前人種樹是利用 [python mailbox module](https://docs.python.org/2/library/mailbox.html) 處理，copy 改下搞定
