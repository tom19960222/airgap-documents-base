---
collection: tocas
version: "5.0.2"
title: "簡短通知 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/5.0/zh-tw/snackbar.html
fetched_at: 2025-03-22T01:53:10+08:00
---
```html
<div class="ts-snackbar">
    <div class="content">你已成功地還原檔案了。</div>
    <button class="action">重新送出</button>
</div>
```

## 概要

適合擺放在角落的通知元件，這和[常駐訊息](notice.md)類似但能擺放動作按鈕。

## 結構

### [文字](snackbar.md#content)

簡短通知最基礎的文字訊息。

```html
<div class="ts-snackbar">
    <div class="content">澳門首家線上賭場上線啦！</div>
</div>
```

### [動作](snackbar.md#action)

帶有動作的簡短通知可以在點擊後執行某項行為。

```html
<div class="ts-snackbar">
    <div class="content">這個檔案已經損毀了。</div>
    <button class="action">移至回收桶</button>
</div>
```

### [關閉按鈕](snackbar.md#close)

擺放關閉按鈕讓使用者能提早關閉通知。

```html
<div class="ts-snackbar">
    <div class="content">檢舉已送出，你會在之後收到電子信件通知。</div>
    <button class="close"></button>
</div>
```

## 外觀

### [負面的](snackbar.md#negative)

表明這個動作執行之後可能有危險、負面或破壞性的意味。

```html
<div class="ts-snackbar">
    <div class="content">你有五則訊息尚未讀取。</div>
    <button class="action is-negative">全部刪除</button>
</div>
```

在尋找相似的元件嗎？

- [常駐訊息](notice.md)
