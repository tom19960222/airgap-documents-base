---
collection: tocas
version: "5.0.2"
title: "檢查清單 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/5.0/zh-tw/checklist.html
fetched_at: 2025-03-22T01:53:10+08:00
---
```html
<div class="ts-checklist">
    <div class="item is-positive">這個電腦符合 Windows 2077 的安裝需求。</div>
    <div class="item is-positive">升級系統的時候將會獲得一隻免費的貓咪。</div>
    <div class="item is-negative">目前還無法升級。</div>
</div>
```

## 項目外觀

### [正面的](checklist.md#positive)

表示這個條件相符或是一個正面的內容。

```html
<div class="ts-checklist">
    <div class="item is-positive">此更新適用於你的裝置。</div>
    <div class="item is-positive">所需的處理器安全性相符。</div>
</div>
```

### [負面的](checklist.md#negative)

表示不相符的條件或是負面的敘述。

```html
<div class="ts-checklist">
    <div class="item is-negative">你的顯示卡等級過於老舊。</div>
    <div class="item is-negative">這個版本無法使用高級功能。</div>
</div>
```

### [注意的](checklist.md#warning)

表示需要額外注意的項目。

```html
<div class="ts-checklist">
    <div class="item is-warning">這個應用程式沒有經過官方驗證。</div>
    <div class="item is-warning">發言前請三思而後行。</div>
</div>
```

### [新增的](checklist.md#added)

自上次以來新增的項目。

```html
<div class="ts-checklist">
    <div class="item is-added">我們增進了系統穩定性。</div>
    <div class="item is-added">提昇操控角色時的移動速度。</div>
</div>
```

### [被移除的](checklist.md#removed)

已經被移除的項目。

```html
<div class="ts-checklist">
    <div class="item is-removed">由於專注輕機槍過多人使用，我們已將其移除。</div>
    <div class="item is-removed">工程師的最高等級從 3 降為 2，因為 Valve 數不到 3。</div>
</div>
```

### [補充資訊的](checklist.md#info)

用以補充額外資訊的項目。

```html
<div class="ts-checklist">
    <div class="item is-info">現已有最新版本可供下載，但你仍可繼續使用。</div>
    <div class="item is-info">這個人試圖保持中立。</div>
</div>
```

在尋找相似的元件嗎？

- [清單](list.md)
