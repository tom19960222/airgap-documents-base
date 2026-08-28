---
collection: tocas
version: "5.7.0"
title: "評分 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/ef8248b165f458215fb8f18bb400c4bfba1767fa/docs/5.7/zh-tw/rating.html
fetched_at: 2026-02-25T00:25:36+08:00
---
```html
<div class="ts-rating is-yellow">
    <div class="star is-active"></div>
    <div class="star is-active"></div>
    <div class="star"></div>
</div>
```

## 種類

### [可供輸入的](rating.md#input)

可讓使用者以點擊的方式輸入評分數值。

```html
<div class="ts-rating is-yellow is-input">
    <input class="star" type="radio" name="rating" value="1">
    <input class="star" type="radio" name="rating" value="2" checked>
    <input class="star" type="radio" name="rating" value="3">
    <input class="star" type="radio" name="rating" value="4">
    <input class="star" type="radio" name="rating" value="5">
</div>
```

## 狀態

### [停用的](rating.md#disabled)

使評分呈現無法互動、點擊的模樣。

```html
<div class="ts-rating is-input is-red">
    <input class="heart" type="radio" name="love" value="1" disabled>
    <input class="heart" type="radio" name="love" value="2" checked disabled>
    <input class="heart" type="radio" name="love" value="3" disabled>
    <input class="heart" type="radio" name="love" value="4" disabled>
    <input class="heart" type="radio" name="love" value="5" disabled>
</div>
```

### [啟用的](rating.md#active)

啟用指定的項目讓使用者得知目前評分為何。

```html
<div class="ts-rating">
    <div class="star is-active"></div>
    <div class="star is-active"></div>
    <div class="star"></div>
</div>
```

### [半星的](rating.md#half)

使某個啟用的星號項目以一半呈現，通常用於帶有小數點的評分。

```html
<div class="ts-rating">
    <div class="star is-active"></div>
    <div class="star is-active is-half"></div>
    <div class="star"></div>
</div>
```

## 結構

### [星號](rating.md#star)

以星星的方式呈現評分。

```html
<div class="ts-rating">
    <div class="star is-active"></div>
    <div class="star"></div>
    <div class="star"></div>
</div>
```

### [愛心](rating.md#heart)

以愛心的方式呈現評分。

```html
<div class="ts-rating">
    <div class="heart is-active"></div>
    <div class="heart"></div>
    <div class="heart"></div>
</div>
```

## 外觀

### [顏色](rating.md#colors)

評分的星星通常會是黃色，愛心則是紅色。

```html
<div class="ts-rating is-yellow">
    <div class="star is-active"></div>
    <div class="star is-active"></div>
    <div class="star"></div>
</div>
<div class="ts-rating is-red">
    <div class="heart is-active"></div>
    <div class="heart"></div>
    <div class="heart"></div>
</div>
```

### [尺寸](rating.md#sizes)

更改評分的大小。

```html
<div class="ts-rating is-yellow is-small">
    <div class="star is-active"></div>
    <div class="star is-active"></div>
    <div class="star"></div>
</div>
<div class="ts-rating is-yellow">
    <div class="star is-active"></div>
    <div class="star is-active"></div>
    <div class="star"></div>
</div>
<div class="ts-rating is-yellow is-large">
    <div class="star is-active"></div>
    <div class="star is-active"></div>
    <div class="star"></div>
</div>
```
