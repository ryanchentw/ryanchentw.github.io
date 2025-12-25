---
title: "Instant Proofreading Using Macos Automator"
date: 2025-12-25T19:56:20+08:00
---


## Introduction
年末了還是來寫一點東西，絕對不是聖誕節沒有人約，只是不想浪費行憲紀念日放假的美好夜晚。

公司有很多外國同事，每天 slack 筆戰總是輸人一截，刷 credit 往往也刷得差強人意，一切的問題根源都是英文訓練不足。

幸好這是美好的 AI 時代，分分鐘請 LLM proofreading 不在話下，打開對話視窗都是一排 proofreading，把我打這個單字的手速鍛鍊的跟拓海的排檔一樣快。

於是痛定思痛，在這個放假的夜晚我悟了，開始找一下有沒有簡單的做法可以做到像 grammarly 以前那樣會飄一個 icon 在 input box 周圍可以按。

問了一下 Claude 解法還真不少，推薦使用 Automator + Keyboard Shortcut 的組合，這樣不只是右鍵選單可以快速呼叫，也可以用系統 global shortcut 來觸發。

原本想直接用 `claude -p` 或是 `gemini -p` 來省錢，但是登入一直搞不定，最後還是寫一個 Python script 串 openai 來處理。

Automator 建立步驟如下：
1. Create Quick Action in Automator
2. Set "Workflow receives" to text
3. Check "Output replaces selected text" ← this is the key setting
4. Add Run Shell Script, set "Pass input" to to stdin



## The code
Python script 參考如下：
```python
import sys
import os
import json

# import duckdb
import urllib.request


def _save_to_duckdb(input_, output):
    conn = duckdb.connect(os.path.expanduser("~/notes/ryan.duckdb"))
    conn.execute("INSERT INTO proofreadings (input, output, created_at) VALUES (?, ?, NOW())", [input_, output])
    conn.close()


def main():
    input_ = sys.stdin.read().strip()

    api_key = "sk-proj-how-do-you-turn-this-on"

    sys_prompt = """
    Proofread and rewrite as a native speaker.

    Rules:
    - Return only the corrected text, nothing else
    - No explanations or suggestions
    - Tone: positive, assertive, optimistic, precise, and upbeat
    """

    req = urllib.request.Request(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        data=json.dumps({
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": f"{sys_prompt}\n\n```{input_}```"}]
        }).encode()
    )

    resp = json.load(urllib.request.urlopen(req))
    output = resp["choices"][0]["message"]["content"]
    # _save_to_duckdb(input_, output)

    # Calculate cost (gpt-4o-mini: $0.15/1M input, $0.60/1M output)
    usage = resp.get("usage", {})
    input_tokens = usage.get("prompt_tokens", 0)
    output_tokens = usage.get("completion_tokens", 0)
    cost = (input_tokens * 0.15 + output_tokens * 0.60) / 1_000_000

    print(f"{output} (${cost:.6f})", end='')

if __name__ == '__main__':
    main()
```

裡面有寫一段 duckdb 順便收集一下資料，不喜歡的可以直接砍掉，接下來設定 macos global level shortcut

System Settings → Keyboard → Keyboard Shortcuts → Services

Steps:
1. Open System Settings
2. Go to Keyboard
3. Click Keyboard Shortcuts...
4. Select Services in the left sidebar
5. Find your action under Text
6. Click none next to it and press your shortcut (e.g., Cmd+Shift+T)


## Conclusion
我是設定 command+option+1，在 slack 輸入框試用幾次效果不得了，回傳直接幫你覆蓋好，整套傳便便，
每天省了幾個 e，我人生完整了，感謝天。
