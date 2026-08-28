---
collection: tocas
version: "5.7.0"
title: "圖片組合 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/ef8248b165f458215fb8f18bb400c4bfba1767fa/docs/5.7/zh-tw/imageset.html
fetched_at: 2026-02-25T00:25:36+08:00
---
```html
<div class="ts-imageset is-3-images">
    <div class="item">
        <img src="image.png">
    </div>
    <div class="item">
        <img src="image.png">
    </div>
    <div class="item">
        <img src="image.png">
    </div>
</div>
```

## 外觀

### [項目數量](imageset.md#images)

指定一個組合裡面有幾張圖片，這是必要的樣式。可用的數量從 `is-1-images` 到 `is-4-images`。

```html
<div class="ts-imageset is-4-images">
    <div class="item">
        <img src="image.png">
    </div>
    <div class="item">
        <img src="image.png">
    </div>
    <div class="item">
        <img src="image.png">
    </div>
    <div class="item">
        <img src="image.png">
    </div>
</div>
```

### [人像的](imageset.md#portrait)

使格局排列以左右呈現，適合用以展示垂直人像的照片。

```html
<div class="ts-imageset is-4-images is-portrait">
    <div class="item">
        <img src="image.png">
    </div>
    <div class="item">
        <img src="image.png">
    </div>
    <div class="item">
        <img src="image.png">
    </div>
    <div class="item">
        <img src="image.png">
    </div>
</div>
```

### [圓角的](imageset.md#rounded)

使每個相片的角落都帶有圓角修飾。

```html
<div class="ts-imageset is-3-images is-rounded">
    <div class="item">
        <img src="image.png">
    </div>
    <div class="item">
        <img src="image.png">
    </div>
    <div class="item">
        <img src="image.png">
    </div>
</div>
```

### [密度](imageset.md#density)

圖片的間距可以更密或是更寬鬆。

```html
<div class="ts-imageset is-portrait is-3-images is-relaxed" style="max-width: 300px">
    <div class="item">
        <img src="image.png">
    </div>
    <div class="item">
        <img src="image.png">
    </div>
    <div class="item">
        <img src="image.png">
    </div>
</div>
<div class="ts-imageset is-portrait is-3-images" style="max-width: 300px">
    <div class="item">
        <img src="image.png">
    </div>
    <div class="item">
        <img src="image.png">
    </div>
    <div class="item">
        <img src="image.png">
    </div>
</div>
<div class="ts-imageset is-portrait is-3-images is-compact" style="max-width: 300px">
    <div class="item">
        <img src="image.png">
    </div>
    <div class="item">
        <img src="image.png">
    </div>
    <div class="item">
        <img src="image.png">
    </div>
</div>
```

在尋找相似的元件嗎？

- [多媒體圖片](image.md)
