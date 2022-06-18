---
title: "MySQL Tuple Comparison Issue"
date: 2017-12-09T13:19:56+08:00
enableDisqus: true
Categories:
  - coding
Tags:
  - MySQL
---

MySQL 5.6 tuple comparison bug

這是一個用 IN clause 比較 primary key 卻得到 full table scan 的故事

![Imgur](https://i.imgur.com/LIOTPaT.jpg)

<!--more-->

tl; dr
```
升級 mysql >= 5.7, 改用 and, or 形式串接條件
```

Tuple Comparison Example
```
select * from users where (first_name, last_name) in (
    ('John', 'Doe'),
    ('Haragaki', 'Yui'),
)
```

一開始直覺寫出 IN 的版本（因為 IN 好棒棒會用 [binary search](https://dev.mysql.com/doc/refman/5.7/en/comparison-operators.html#function_in)），結果 explain check 一看居然是 full table scan，昏倒。
想一下用 and + or 串接改看看
```
select * from users where
    (first_name='John' and last_name='Doe') or
    (first_name='Haragaki' and last_name='Yui')
)
```
哎唷不錯喔有吃到 index，就這樣先把 fix 丟上線。

過陣子比較閒來挖一下問題出在哪

翻到 [stackoverflow](https://stackoverflow.com/questions/16117492/different-approach-of-using-in-clause-in-mysql) 上的相關討論，列舉出 IN clause 的幾種使用方式，正是他說的第三種 tuple comparison
後面評論也給出 Percona [一篇文章](https://www.percona.com/blog/2008/04/04/multi-column-in-clause-unexpected-mysql-issue/)

指出是個 bug，而且這邊還是 2008 年的文章，一個好的 bug 果然是歷久彌新

懶得架環境，用[線上環境](https://www.db-fiddle.com/f/xpwiDid8dxHFVvKfD2sgxW/0)測一下，
看其他版本有沒有這問題。

看起來在 MySQL 5.7 解決了，不巧公司用的是 5.6 只好先繼續用 workaround 耶嘿嘿


Ref:

- https://stackoverflow.com/questions/16117492/different-approach-of-using-in-clause-in-mysql
- https://www.percona.com/blog/2008/04/04/multi-column-in-clause-unexpected-mysql-issue/
- https://www.db-fiddle.com/f/xpwiDid8dxHFVvKfD2sgxW/0
