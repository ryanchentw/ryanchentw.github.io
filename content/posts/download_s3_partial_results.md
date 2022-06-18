---
title: "Download s3 partial results"
date: 2020-12-21T11:33:36+08:00
enableDisqus: true

Categories:
  - coding
---

S3 does support the HTTP [range request](https://developer.mozilla.org/en-US/docs/Web/HTTP/Range_requests)

It’s useful when you want the partial lines from a big file.

By aws [s3 command line](https://docs.aws.amazon.com/cli/latest/reference/s3api/get-object.html)

```sh
aws s3api get-object --range bytes=0-10000 --bucket=[BUCKET] --key=[KEY] partial_results
```
