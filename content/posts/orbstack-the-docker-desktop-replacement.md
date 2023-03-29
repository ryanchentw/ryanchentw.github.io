---
title: "Orbstack the Docker Desktop Replacement"
date: 2023-03-29T09:28:43+08:00
---

身為一個資料水管工，在開發的時候常常需要用 docker compose 把整套 Airflow 拉起來測試，

這時候我的 intel-based 筆電常常就會起飛，在咖啡廳都被路人瞪，讓我非常不好意思。


昨天試玩了一下 [OrbStack](https://orbstack.dev/)，覺得好棒棒

第一點是 OrbStack 啟動速度超級快！

以前覺得 Docker Desktop 記憶體吃太兇的時候就想讓他重開，要等等上一分鐘，

現在 OrbStack 啟動只要數秒，連偷個懶都不行，很不方便。

再來是資源使用率部分，

Memory 顯著有感，以前大概會吃到 10G swap，換了之後大概只吃到 3G，

CPU 部分也滿不錯，之前開 Docker Desktop 的時候其他東西都會比較卡，

開發體驗很差，索性開發完才拉起來測試，現在可以邊跑邊開發了，法喜充滿。


轉換的痛點
- 需要升級到 macOS Ventura (13.2?)
- 所有 image 要重 build


behind the scenes
- [背後的原理](https://docs.orbstack.dev/architecture)，是利用 macOS Ventura 提供的 Virtualization Framework，share kernel 跟 windows 的 WSL2 很像
- [未來會收錢](https://docs.orbstack.dev/faq#free)，且用且珍惜


![memory](https://i.imgur.com/MMTcw9f.png)
