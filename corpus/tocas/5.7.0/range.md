---
collection: tocas
version: "5.7.0"
title: "範圍滑桿 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/ef8248b165f458215fb8f18bb400c4bfba1767fa/docs/5.7/zh-tw/range.html
fetched_at: 2026-02-25T00:25:36+08:00
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
