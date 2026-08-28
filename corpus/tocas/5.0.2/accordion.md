---
collection: tocas
version: "5.0.2"
title: "可折疊內容 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/5.0/zh-tw/accordion.html
fetched_at: 2025-03-22T01:53:10+08:00
---
```html
<details class="ts-accordion" open>
    <summary>營業時間為何？</summary>
    每日的早上九點至晚上八點。
</details>
```

## 概要

可折疊內容使用 `<details>` HTML 標籤，因此支援瀏覽器原生的 [`toggle`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDetailsElement/toggle_event) 事件以監聽其開關狀態。

## 狀態

### [打開的](accordion.md#open)

當可折疊內容被指定 `[open]` 的時候，瀏覽器就會顯示其內容。

```html
<details class="ts-accordion" open>
    <summary>當我使用 API 的時候，是否有提供 SSL 加密傳輸協定？</summary>
    無，本銀行全面採用非加密的 HTTP 傳統標準通訊協定。
</details>
```

### [群組的](accordion.md#name)

相同 `[name]` 的可折疊內容會被視為同個群組，同個群組裡同時只能展開一個可折疊內容。Firefox 目前尚未支援此功能。

```html
<details class="ts-accordion" name="help">
    <summary>此遊戲可在哪些作業系統上遊玩？</summary>
    支援 Linux、Windows、macOS 與 Steam OS。
</details>
<div class="ts-divider is-section"></div>
<details class="ts-accordion" name="help">
    <summary>遊戲的檔案大小為何？</summary>
    若要安裝此遊戲，請確保至少有 20 GB 的可用空間。
</details>
```
