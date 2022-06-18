---
title: "重寫所有 git author name & email"
date: 2022-06-18T10:48:54+08:00
enableDisqus: true
---

在家工作之後，幾乎都是用公司筆電，一些個人專案不小心套到公司 email 設定，
想說可能要寫個 script 來處理，沒想到一行就解決了。


```bash
git config --local user.name "Kaneshiro Takeshi"
git config --local user.email "your_email@example.com"
git rebase --root --exec 'git commit --amend --no-edit --reset-author'
```
