---
collection: tocas
version: "5.7.0"
title: "常駐訊息 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/ef8248b165f458215fb8f18bb400c4bfba1767fa/docs/5.7/zh-tw/notice.html
fetched_at: 2026-02-25T00:25:36+08:00
---
```html
<div class="ts-notice">
    <div class="title">看過來</div>
    <div class="content">請收起側腳架並按住煞車與 GO 按鍵重新啟動馬達。</div>
</div>
```

## 概要

常駐訊息通常會在執行完某個動作之後出現，如：表單成功送出、刪除失敗。

## 外觀

### [外框線的](notice.md#outlined)

僅描繪訊息的外框線使其看起來較沒有那麼顯眼。

```html
<div class="ts-notice is-outlined">
    <div class="title">測試階段</div>
    <div class="content">
        目前網站正在進行測試，若有任何不穩定現象請稍待數分鐘即會恢復正常。
    </div>
</div>
```

### [負面的](notice.md#negative)

帶有危險意味的訊息。

```html
<div class="ts-notice is-negative">
    <div class="title">刪除失敗</div>
    <div class="content">若要刪除此資料夾，請先清空內部的所有檔案。</div>
</div>
```

### [尺寸](notice.md#sizes)

更改常駐訊息的大小。

```html
<div class="ts-notice is-small">
    <div class="title">小型訊息</div>
    <div class="content">這裡是一段文字訊息。</div>
</div>
<div class="ts-notice">
    <div class="title">預設訊息</div>
    <div class="content">這裡是一段文字訊息。</div>
</div>
<div class="ts-notice is-large">
    <div class="title">大型訊息</div>
    <div class="content">這裡是一段文字訊息。</div>
</div>
```

在尋找相似的元件嗎？

- [簡短通知](snackbar.md)
