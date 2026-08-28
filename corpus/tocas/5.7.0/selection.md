---
collection: tocas
version: "5.7.0"
title: "項目切換 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/ef8248b165f458215fb8f18bb400c4bfba1767fa/docs/5.7/zh-tw/selection.html
fetched_at: 2026-02-25T00:25:36+08:00
---
```html
<div class="ts-selection">
    <label class="item">
        <input type="radio" name="aircon" checked>
        <div class="text">冷氣</div>
    </label>
    <label class="item">
        <input type="radio" name="aircon">
        <div class="text">暖氣</div>
    </label>
    <label class="item">
        <input type="radio" name="aircon">
        <div class="text">送風</div>
    </label>
</div>
```

## 概要

這個元件能在不同選項中來回切換。如果希望用來切換內容，請使用[分頁籤](tab.md)。

## 狀態

### [停用的](selection.md#disabled)

使項目選擇呈現無法互動、點擊的模樣。

```html
<div class="ts-selection">
    <label class="item">
        <input type="radio" name="version" disabled>
        <div class="text">標準</div>
    </label>
    <label class="item">
        <input type="radio" name="version" checked>
        <div class="text">進階</div>
    </label>
    <label class="item">
        <input type="radio" name="version">
        <div class="text">測試</div>
    </label>
</div>
```

## 外觀

### [圓角的](selection.md#circular)

將邊緣角落以圓角處理。

```html
<div class="ts-selection is-circular">
    <label class="item">
        <input type="radio" name="audio" checked>
        <div class="text">低音</div>
    </label>
    <label class="item">
        <input type="radio" name="audio">
        <div class="text">中音</div>
    </label>
    <label class="item">
        <input type="radio" name="audio">
        <div class="text">高音</div>
    </label>
</div>
```

### [流動的](selection.md#fluid)

項目切換的寬度可以填滿父容器。

```html
<div class="ts-selection is-fluid">
    <label class="item">
        <input type="radio" name="language">
        <div class="text">台灣正體</div>
    </label>
    <label class="item">
        <input type="radio" name="language" checked>
        <div class="text">英文</div>
    </label>
    <label class="item">
        <input type="radio" name="language">
        <div class="text">日本語</div>
    </label>
</div>
```

### [尺寸](selection.md#sizes)

更改項目切換的大小。

```html
<div class="ts-selection is-small">
    <label class="item">
        <input type="radio" name="size-1" checked>
        <div class="text">小型項目</div>
    </label>
    <label class="item">
        <input type="radio" name="size-1">
        <div class="text">小型項目</div>
    </label>
</div>
<div class="ts-selection">
    <label class="item">
        <input type="radio" name="size-2" checked>
        <div class="text">預設項目</div>
    </label>
    <label class="item">
        <input type="radio" name="size-2">
        <div class="text">預設項目</div>
    </label>
</div>
<div class="ts-selection is-large">
    <label class="item">
        <input type="radio" name="size-3" checked>
        <div class="text">大型項目</div>
    </label>
    <label class="item">
        <input type="radio" name="size-3">
        <div class="text">大型項目</div>
    </label>
</div>
```

### [密度](selection.md#density)

在不改變文字大小的情況下變更項目切換的高度，看起來更緊密或是令人感到寬鬆。

```html
<div class="ts-selection is-dense">
    <label class="item">
        <input type="radio" name="density-1" checked>
        <div class="text">緊密項目</div>
    </label>
    <label class="item">
        <input type="radio" name="density-1">
        <div class="text">緊密項目</div>
    </label>
</div>
<div class="ts-selection">
    <label class="item">
        <input type="radio" name="density-2" checked>
        <div class="text">預設項目</div>
    </label>
    <label class="item">
        <input type="radio" name="density-2">
        <div class="text">預設項目</div>
    </label>
</div>
<div class="ts-selection is-relaxed">
    <label class="item">
        <input type="radio" name="density-3" checked>
        <div class="text">寬鬆項目</div>
    </label>
    <label class="item">
        <input type="radio" name="density-3">
        <div class="text">寬鬆項目</div>
    </label>
</div>
```

在尋找相似的元件嗎？

- [核取方塊](checkbox.md)
- [關聯標籤](chip.md)
- [單選方塊](radio.md)
- [分頁籤](tab.md)
