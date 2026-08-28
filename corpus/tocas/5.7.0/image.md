---
collection: tocas
version: "5.7.0"
title: "多媒體圖片 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/ef8248b165f458215fb8f18bb400c4bfba1767fa/docs/5.7/zh-tw/image.html
fetched_at: 2026-02-25T00:25:36+08:00
---
```html
<div class="ts-image">
    <img src="image.png" width="150">
</div>
```

## 概要

圖片預設會填滿父容器的寬度，若要變更圖片的尺寸，請在 `<img>` 標籤指定寬高。

## 狀態

### [停用的](image.md#disabled)

表示這個圖片已經無法互動、不再可用了。

```html
<div class="ts-image is-disabled">
    <img src="image.png" width="150">
</div>
```

## 外觀

### [圓角的](image.md#rounded)

使四個角落都變得稍微有點圓角修飾。

```html
<div class="ts-image is-rounded">
    <img src="image.png" width="150">
</div>
```

### [圓形的](image.md#circular)

將整張圖片變為圓形，只有在圖片是正方形的情況下才會生效。

```html
<div class="ts-image is-circular">
    <img src="image.png" width="150">
</div>
```

### [邊框的](image.md#bordered)

使圖片帶有邊框，適合用於白底圖片讓使用者知道其邊界在哪。

```html
<div class="ts-image is-bordered">
    <img src="image.png" width="150">
</div>
```

### [置中的](image.md#centered)

水平左右置中一張圖片。

```html
<div class="ts-image is-centered">
    <img src="image.png" width="150">
</div>
```

### [裁切的](image.md#covered)

不論是什麼長寬比都不會變形而會自動裁切其內容。

```html
<div class="ts-image is-covered">
    <img src="image.png" width="100" height="100">
</div>
```

### [長寬比的](image.md#aspect-ratios)

將圖片以 `1:1`、`4:3`、`16:9` 的方式呈現，超出的部份會被裁切。

```html
<div class="ts-image is-1-by-1">
    <img src="image.png" width="200">
</div>
<div class="ts-image is-4-by-3">
    <img src="image.png" width="200">
</div>
<div class="ts-image is-16-by-9">
    <img src="image.png" width="200">
</div>
```

### [間隔的](image.md#spaced)

在前或後新增間隔以避免與其他元件相鄰太近。

```html
相較於稱呼自己是間「科技公司」，我們
<div class="ts-image is-start-spaced">
    <img src="image.png" width="35">
</div>
的運作模式更像是所「學校」。雖然卡莉絲伊繁星提供網際網路服務與電子科技產業的相關產品，但我們更注重人們是否能在開發的過程
<div class="ts-image is-end-spaced">
    <img src="image.png" width="35">
</div>
中有所收穫並學以致用，而我們也十分地重視一項產品是否能夠達成社會的期許並希望能藉此改變某些人的生活，協助大眾
<div class="ts-image is-spaced">
    <img src="image.png" width="35">
</div>
更向自己的目標邁進；這也正是伊繁星最高協議被創造的原因。
```

在尋找相似的元件嗎？

- [圖片組合](imageset.md)
