---
title: "抓網站內容做成電子書 (epub)"
date: 2022-06-18T11:52:41+08:00
---

![alt](https://i.imgur.com/MnSCg5R.jpg)

買了 BOOX note5 之後, 覺得電子紙螢幕呈現效果真舒服, 所有要長時間閱讀的東西都想丟進去.
另外發現雖然系統用 Android 11, 理論上可以裝所有 Android App, 包含瀏覽器,
不過在裝了一堆 App 發現都是虛幻, 排版與文字呈現還是用 epub 格式最好.

本次範例使用 [EbookLib](https://pypi.org/project/EbookLib/), [requests](https://pypi.org/project/requests/)

以及 mark_mew 大大的[關於我幫新公司建立整套部屬流程那檔事](https://ithelp.ithome.com.tw/users/20141518/ironman/4653) 為範例
感謝 mark_mew 大大分享自身經驗

另外粗粗產生出來的 epub 還是有很多排版問題要修, 像是圖片不見了, script tag 跑出來了, 在過一層 strip_tags 應該會好一點.
看來最適合的還是轉小說進去 (?

這次網頁數量不多用 requests 抓抓就好, 就不寫 scrapy 了, 抓別人網站注意禮貌

程式分成四段, 第四段跟 ebooklib 範例程式只有差異在產生 sections 部分
- 抓內容網址
- 抓內容 -> local file
- 建立章節
- 寫成 epub


```python
from ebooklib import epub
from lxml.html import fromstring
from tqdm import tqdm
import os
import requests

# 抓內容的網址
urls = []
headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
}
page_urls = [
    'https://ithelp.ithome.com.tw/users/20141518/ironman/4653',
    'https://ithelp.ithome.com.tw/users/20141518/ironman/4653?page=2',
    'https://ithelp.ithome.com.tw/users/20141518/ironman/4653?page=3',
]
for url in tqdm(page_urls):
    response = requests.get(url, headers=headers)
    tree = fromstring(response.text)
    urls += [s.strip() for s in tree.xpath('//h3[@class="qa-list__title"]/a/@href')]

# 抓內容
for url in tqdm(urls):
    fname = url.split('/')[-1]
    with open(fname, 'w') as wf:
        response = requests.get(url, headers=headers)
        wf.write(response.text)

# 建立章節
def build_sections():
    sections = []
    for fname in tqdm(sorted(os.listdir('./ebooks'))):  # 利用檔案名稱排章節順序
        if '.' in fname:
            continue
        with open('./ebooks/' + fname) as f:
            tree = fromstring(f.read())
            title = tree.xpath('//h2[@class="qa-header__title ir-article__title"]/text()')[0].strip()
            content = ''.join(list(tree.xpath('//div[@class="qa-panel__content"]')[0].itertext()))
            content = content.replace('\n', '<br/>')
            section = epub.EpubHtml(title=title, file_name=fname, lang='zh-hant')
            section.content = content
            sections.append(section)
    return build_sections

# 寫成 epub
from ebooklib import epub

book = epub.EpubBook()

# set metadata
book.set_identifier('ithome_ironman_4653')
book.set_title('關於我幫新公司建立整套部屬流程那檔事')
book.set_language('zh-hant')
book.add_author('mark_mew')


# create chapter
sections = build_sections()

# add chapter
for section in sections:
    book.add_item(section)

# define Table Of Contents
book.toc = [
    epub.Link(section.file_name, section.title, section.title)
    for section in sections
]

# add default NCX and Nav file
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())

# define CSS style
style = 'BODY {color: white;}'
nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)

# add CSS file
book.add_item(nav_css)

# basic spine
book.spine = ['nav'] + sections

# write to the file
epub.write_epub('關於我幫新公司建立整套部屬流程那檔事.epub', book, {})
```
