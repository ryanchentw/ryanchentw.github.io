---
title: "打包 markdown 筆記並上傳到 R2 (S3 like service)"
date: 2022-08-20T15:22:09+08:00
---

自從用 markdown 開始寫工作日誌與筆記，一直放在 iCloud 上面，之前看到 iCloud 掉資料的新聞覺得好像還是有必要多異地備份一下，那時候選了 S3，看重的當然是 11 nines 的耐用性，這樣畢生筆記萬無一失了吧。

這陣子發現 Cloudflare 的 R2 可以開始用 [beta](https://blog.cloudflare.com/r2-open-beta/) 版本了，基於我本人是 Cloudflare 無腦粉，馬上就想把目前的筆記也丟一份放在上面，於是就來研究一下。

首先 Cloudflare R2 跟 S3 一樣是 11 nines，對外宣稱的耐用性跟 S3 一樣，再來是每 GB 價錢，R2 目前是 $0.015 per GB per month，跟 S3 Virginia $0.023 比起來低了 35%，再來是資料不收輸出的頻寬費用，這點我自己很好奇，那不就可以拿來做一個免費的圖床？最後是跟 s3 相容的 api 把 api token 申請好之後就可以直接用 aws cli 上傳檔案。

一開始到 [https://dash.cloudflare.com/sign-up/r2](https://dash.cloudflare.com/sign-up/r2) 申請服務，可以看到開 bucket 是不用選 region 的，下面說明 `R2 buckets are automatically distributed across Cloudflare's data centers` 另外也注意到 bucket name 應該是帳號內不能相同，跟 AWS 整個 region 不能有相同的 bucket name 不一樣。

![create bucket](https://i.imgur.com/olqi0fC.png)

開完 bucket 之後開始處理懶人指令的部分
1. 註冊 API token
2. aws configure 設定
3. 複製 Account ID
4. 假設你的筆記資料夾在 `notes/`, 上傳到 {bucket_name}, 使用 {account_id} 的 R2 endpoint

最後懶人指令會長這樣
```sh
export FILENAME=notes_$(date +"%Y-%m-%d").tar.xz; \
tar -chJf $FILENAME notes/ && \
aws s3api put-object --bucket {bucket_name} --key $FILENAME --body $FILENAME --endpoint-url https://{account_id}.r2.cloudflarestorage.com
```
![api token](https://i.imgur.com/6a9gpIs.png)
![aws configure](https://i.imgur.com/3AhN3IY.png)

refs.
- https://developers.cloudflare.com/r2/examples/aws-cli/
