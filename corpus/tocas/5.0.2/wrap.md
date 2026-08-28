---
collection: tocas
version: "5.0.2"
title: "間隔容器 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/5.0/zh-tw/wrap.html
fetched_at: 2025-03-22T01:53:10+08:00
---
```html
<div class="ts-wrap">
    <button class="ts-button">按鈕</button>
    <button class="ts-button">按鈕</button>
    <button class="ts-button">按鈕</button>
</div>
```

## 概要

元件裡的項目會自動以空白區隔，項目會在過寬時自動換行。若希望某個項目可以填滿剩餘空間，請使用[網格系統](grid.md)。

## 外觀

### [垂直的](wrap.md#vertical)

將排列的方向改為上下垂直。

```html
<div class="ts-wrap is-vertical">
    <button class="ts-button">按鈕</button>
    <button class="ts-button">按鈕</button>
    <button class="ts-button">按鈕</button>
</div>
```

### [水平對齊](wrap.md#horizontal-aligns)

項目可以選擇靠左、中或右對齊。

```html
<div class="ts-wrap is-start-aligned">
    <button class="ts-button">置左對齊</button>
</div>
<div class="ts-wrap is-center-aligned">
    <button class="ts-button">置中對齊</button>
</div>
<div class="ts-wrap is-end-aligned">
    <button class="ts-button">置右對齊</button>
</div>
```

### [垂直對齊](wrap.md#vertical-aligns)

根據項目之間的高度，可以更改其上、中或下對齊方式。

```html
<div class="ts-wrap is-top-aligned">
    <div class="ts-box has-padded" style="width: 30%">
        Consectetur adipiscing elit. In fermentum metus dolor.
    </div>
    <div class="ts-box has-padded" style="width: 30%">
        置上對齊
    </div>
    <div class="ts-box has-padded" style="width: 30%">
        Consectetur adipiscing elit. In fermentum metus dolor.
    </div>
</div>
<div class="ts-wrap is-middle-aligned">
    <div class="ts-box has-padded" style="width: 30%">
        Consectetur adipiscing elit. In fermentum metus dolor.
    </div>
    <div class="ts-box has-padded" style="width: 30%">
        置中對齊
    </div>
    <div class="ts-box has-padded" style="width: 30%">
        Consectetur adipiscing elit. In fermentum metus dolor.
    </div>
</div>
<div class="ts-wrap is-bottom-aligned">
    <div class="ts-box has-padded" style="width: 30%">
        Consectetur adipiscing elit. In fermentum metus dolor.
    </div>
    <div class="ts-box has-padded" style="width: 30%">
        置下對齊
    </div>
    <div class="ts-box has-padded" style="width: 30%">
        Consectetur adipiscing elit. In fermentum metus dolor.
    </div>
</div>
```

### [密度](wrap.md#density)

欄位的間距可以更密或是更寬鬆。

```html
<div class="ts-wrap is-relaxed">
    <button class="ts-button">項目</button>
    <button class="ts-button">項目</button>
</div>
<div class="ts-wrap">
    <button class="ts-button">項目</button>
    <button class="ts-button">項目</button>
</div>
<div class="ts-wrap is-compact">
    <button class="ts-button">項目</button>
    <button class="ts-button">項目</button>
</div>
```

## 組合應用

### [關聯標籤](wrap.md#composition-chip)

標籤元件就算換行，也能保持一定的空白間隔。

```html
<div class="ts-wrap is-compact">
    <div class="ts-chip">
        <img src="user.png"> Yami Odymel
    </div>
    <div class="ts-chip">
        <img src="user.png"> Henry Wu
    </div>
    <div class="ts-chip">
        <img src="user.png"> Sean
    </div>
    <div class="ts-chip">
        <img src="user.png"> Ming Tsay
    </div>
    <div class="ts-chip">
        <img src="user.png"> Mac Taylor
    </div>
    <div class="ts-chip">
        <img src="user.png"> Tsundere Chen
    </div>
</div>
```

### [表單欄位](wrap.md#composition-form)

透過間隔容器讓表單欄位保持一定空白距離。

```html
<div class="ts-wrap is-vertical">
    <div class="ts-text is-label">使用者帳號</div>
    <div class="ts-input is-start-icon">
        <span class="ts-icon is-user-icon"></span>
        <input type="text">
    </div>
    <div class="ts-text is-label">密碼</div>
    <div class="ts-input is-start-icon">
        <span class="ts-icon is-lock-icon"></span>
        <input type="password">
    </div>
</div>
```

## 樣式變數

|  | 說明 | 預設值 | 目標 |
| --- | --- | --- | --- |
| --gap | 項目之間的空白間隙寬度。 | `1rem` | `.ts-wrap` |

在尋找相似的元件嗎？

- [網格系統](grid.md)
