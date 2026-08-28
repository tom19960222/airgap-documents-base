---
collection: tocas
version: "5.7.0"
title: "內容遮罩 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/ef8248b165f458215fb8f18bb400c4bfba1767fa/docs/5.7/zh-tw/mask.html
fetched_at: 2026-02-25T00:25:36+08:00
---
```html
<div class="ts-image">
    <img src="image.png" style="max-width: 450px">
    <div class="ts-mask is-centered">
        <div class="ts-loading is-large"></div>
    </div>
</div>
```

## 外觀

### [半部的](mask.md#partially)

遮罩可以只覆蓋父容器的上、中、下部份。

```html
<div class="ts-image">
    <img src="image.png" style="max-width: 450px">
    <div class="ts-mask is-top">
        <div class="ts-content">
            <div class="ts-header">置上遮罩</div>
            然後這裡會放一段文字。
        </div>
    </div>
</div>
<div class="ts-image">
    <img src="image.png" style="max-width: 450px">
    <div class="ts-mask is-middle">
        <div class="ts-content">
            <div class="ts-header">置中遮罩</div>
            然後這裡會放一段文字。
        </div>
    </div>
</div>
<div class="ts-image">
    <img src="image.png" style="max-width: 450px">
    <div class="ts-mask is-bottom">
        <div class="ts-content">
            <div class="ts-header">置底遮罩</div>
            然後這裡會放一段文字。
        </div>
    </div>
</div>
```

### [內容置中的](mask.md#centered)

置中遮罩的內容，適合用來擺放[讀取狀態](loading.md)。

```html
<div class="ts-image">
    <img src="image.png" style="max-width: 450px">
    <div class="ts-mask is-centered">
        <div class="ts-loading is-large"></div>
    </div>
</div>
```

### [淡化的](mask.md#faded)

遮罩可以處於父容器的上、中、下部份。

```html
<div class="ts-image">
    <img src="image.png" style="max-width: 450px">
    <div class="ts-mask is-faded is-top">
        <div class="ts-content">
            <div class="ts-header">置上遮罩</div>
            然後這裡會放一段文字。
        </div>
    </div>
</div>
<div class="ts-image">
    <img src="image.png" style="max-width: 450px">
    <div class="ts-mask is-faded is-bottom">
        <div class="ts-content">
            <div class="ts-header">置底遮罩</div>
            然後這裡會放一段文字。
        </div>
    </div>
</div>
```

### [次要的](mask.md#secondary)

沒有背景的遮罩會顯得不重要，但可以用來呈現內容在某些物件上。

```html
<div class="ts-image">
    <img src="image.png" style="max-width: 450px">
    <div class="ts-mask is-secondary is-bottom">
        <div class="ts-content" style="color: #333">
            <div class="ts-header">限時特價</div>
            現在購買這個蛋糕只需要新台幣 3,000 元！
        </div>
    </div>
</div>
```

### [模糊的](mask.md#blurring)

被遮蔽的內容能夠以模糊化處理。

```html
<div class="ts-image">
    <img src="image.png" style="max-width: 450px">
    <div class="ts-mask is-blurring"></div>
</div>
```

## 組合應用

### [關閉按鈕](mask.md#composition-close)

透過搭配遮罩與關閉按鈕可以讓圖片的右上角有個常見的移除、關閉動作。

```html
<div class="ts-image is-rounded">
    <img src="image.png" width="150">
    <div class="ts-mask is-secondary is-top">
        <div class="ts-content is-compact is-end-aligned has-leading-none">
            <button class="ts-close"></button>
        </div>
    </div>
</div>
```

### [附屬資訊](mask.md#composition-additional-information)

圖片的右下角可以擺放時間或是檔案大小。

```html
<div class="ts-image is-rounded">
    <img src="image.png" width="150">
    <div class="ts-mask is-secondary is-bottom">
        <div class="ts-content is-compact is-end-aligned">
            <div class="ts-badge">32 KB</div>
        </div>
    </div>
</div>
```
