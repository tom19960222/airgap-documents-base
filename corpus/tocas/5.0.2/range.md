---
collection: tocas
version: "5.0.2"
title: "範圍滑桿 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/5.0/zh-tw/range.html
fetched_at: 2025-03-22T01:53:10+08:00
---
```html
<div class="ts-range">
    <input type="range">
</div>
```

## 種類

### [步進的](range.md#step)

指定 `[step]` 屬性可以讓數值以指定間隔進行變動。

```html
<div class="ts-range">
    <input type="range" min="0" max="5" step="1">
</div>
```

## 狀態

### [停用的](range.md#disabled)

使範圍滑桿呈現無法互動、點擊的模樣。

```html
<div class="ts-range">
    <input type="range" disabled>
</div>
```
