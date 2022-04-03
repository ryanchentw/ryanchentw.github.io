---
title: "Terminal Notify"
date: 2017-12-26T09:57:45+08:00
Categories:
  - coding
---

最近公司 build tool 因為專案爆肥越來越慢，build code 要花個十分鐘左右，不太行啊， ~泡咖啡時間變長了呀逼~

<!--more-->

不過暫時沒有時間去優化他，同事提出一個
```
build-code && printf '\a'
```

build 完扣給你逼一下

這招透過 SSH 連進去當然不會逼，如果用 iTerm2 就是意思意思閃一下並亮個紅燈給你看

但是好像還是要喵一下 session tab or Dock icon，似乎不是很方便啊

這時候另一個同事又提出用 [speech-dispatcher](https://devel.freebsoft.org/speechd) 跟 [say](https://developer.apple.com/legacy/library/documentation/Darwin/Reference/ManPages/man1/say.1.html) 講話給你聽

欸，這想法蒸蚌！

不過這玩意 via SSH 不 work 啊！覺得聲音通知是 developer 的未來的我在 Google 努力找尋其他方法。

後來想到 iterm2 好像有功能可以抓 output 來觸發事件，組了一下確實會動，抓 build tool 最後的 Success 文字

config 像這樣，build 完之後就會聲音通知你了哦，就像請了一位秘書呢 ^.<
![Imgur](https://i.imgur.com/TGaTOFA.png)


列出支援的聲音檔，廣東話豪可愛ㄛ
```
> say -v '?'
Mei-Jia             zh_TW    # 您好，我叫美佳。我說國語。
Sin-ji              zh_HK    # 您好，我叫 Sin-ji。我講廣東話。
Ting-Ting           zh_CN    # 您好，我叫Ting-Ting。我讲中文普通话。
```


Ref:

- [iTerm2 triggers](https://www.iterm2.com/documentation-triggers.html)
- [macOS push notification](https://github.com/julienXX/terminal-notifier)
