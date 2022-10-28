---
title: "BigQuery JSON_VALUE_ARRAY, JSON_QUERY_ARRAY 差異跟小雷"
date: 2022-10-28T11:45:27+08:00
---

JSON_VALUE_ARRAY 只吃 scalar value

任何不在 {string, number,boolean} 都會變成 NULL, 像是

```sql
select JSON_VALUE_ARRAY('{"product_ids": [UCCU]}', "$.product_ids");

--
Row	f0_	
1	null
```

但如果裡面有 NULL 則會噴錯
```sql
select JSON_VALUE_ARRAY('{"product_ids": [null]}', "$.product_ids");
```

> Array cannot have a null element; error in writing field f0_

啊如果我就是要 scalar value 裡面又可能有 null 怎麼辦？
這邊可以改用 [JSON_QUERY_ARRAY](https://cloud.google.com/bigquery/docs/reference/standard-sql/json_functions#function_overview) 替代，但因為 output 不同（多了 double quote），視資料情況可以直接 trim 掉處理
```sql
SELECT
    ARRAY(SELECT TRIM(item, '"')
FROM
    UNNEST(JSON_QUERY_ARRAY('{"product_ids": [null, 1, 2, 3]}', "$.product_ids")) AS item);
```
