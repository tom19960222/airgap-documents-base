---
collection: tocas
version: "5.0.2"
title: "標題 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/5.0/zh-tw/header.html
fetched_at: 2025-03-22T01:53:10+08:00
---
```html
<div class="ts-header">「你只能死一次，一定要死的轟轟烈烈。」</div>
```

## 概要

這個元件與[文字](text.md)十分相似，但預設會以較大的字體尺寸呈現並允許帶有圖示或子標題。

## 外觀

### [圖示的](header.md#icon)

帶有象徵圖示的標題同時會置中。

```html
<div class="ts-header is-icon">
    <span class="ts-icon is-users-icon"></span>
    使用者群組
</div>
```

### [側邊圖示的](header.md#side-icon)

在側邊擺放象徵圖示的標題。

```html
<div class="ts-header is-start-icon">
    <span class="ts-icon is-plug-icon"></span>
    99.9% 保證穩定上線
</div>
```

### [沈重的](header.md#heavy)

以最粗的方式標註某段文字。

```html
<div class="ts-header is-heavy">今天是芥末日！</div>
```

### [負面的](header.md#negative)

含有危險、負面意味標語。

```html
<div class="ts-header is-negative">刪除檔案手續</div>
```

### [次要的](header.md#secondary)

用以呈現較不重要的標題，例如：子標題。

```html
<div class="ts-header is-secondary">從資料庫中建立一個全新的使用者。</div>
```

### [截斷的](header.md#truncated)

文字超過一定寬度之後就會被截斷而不會換行或溢出，通常父容器需要有個固定寬度。

```html
<div class="ts-header is-truncated">豔陽高照，前方的道路什麼都看不見。明明不清楚前方的事物，卻感覺自己正在邁向的是一個新世界。</div>
```

### [大、小寫的](header.md#uppercased-and-lowercased)

強制使某段文字大小寫，僅能用於英文。

```html
<div class="ts-header is-uppercased">Update Avatar</div>
<div class="ts-header is-lowercased">Update Avatar</div>
```

### [對齊](header.md#aligns)

更改文字的對齊方式。

```html
<div class="ts-header is-start-aligned">置起始位置</div>
<div class="ts-header is-center-aligned">置中對齊</div>
<div class="ts-header is-end-aligned">置結束位置</div>
```

### [尺寸](header.md#sizes)

相較於其他元件，標題有更多的大小尺寸可供選擇。

```html
<div class="ts-header">(預設) Tocas UI 來自台灣。</div>
<div class="ts-header is-large">(大的) Tocas UI 來自台灣。</div>
<div class="ts-header is-big">(更大) Tocas UI 來自台灣。</div>
<div class="ts-header is-huge">(巨大) Tocas UI 來自台灣。</div>
<div class="ts-header is-massive">(重量級) Tocas UI 來自台灣。</div>
```

在尋找相似的元件嗎？

- [文字](text.md)
