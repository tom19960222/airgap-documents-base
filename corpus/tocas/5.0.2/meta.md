---
collection: tocas
version: "5.0.2"
title: "中繼資料 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/5.0/zh-tw/meta.html
fetched_at: 2025-03-22T01:53:10+08:00
---
```html
<div class="ts-meta">
    <a class="item">使用者條約</a>
    <a class="item">隱私政策</a>
    <a class="item">聯繫我們</a>
</div>
```

## 外觀

### [次要的](meta.md#secondary)

使其文字顏色變得更不顯眼。

```html
<div class="ts-meta is-secondary">
    <a class="item">天野望</a>
    <a class="item">火井向百合</a>
    <a class="item">成海遙香</a>
</div>
```

### [連結的](meta.md#link)

項目的文字能以連結顏色呈現。

```html
<div class="ts-meta is-link">
    <a class="item">支援</a>
    <a class="item">統計資料</a>
    <a class="item">關於</a>
</div>
```

### [文字對齊](meta.md#aligns)

更改文字的對齊方式。

```html
<div class="ts-meta is-start-aligned">
    <a class="item">置起始位置</a>
    <a class="item">置起始位置</a>
</div>
<div class="ts-meta is-center-aligned">
    <a class="item">我置中</a>
    <a class="item">我置中</a>
</div>
<div class="ts-meta is-end-aligned">
    <a class="item">置結束位置</a>
    <a class="item">置結束位置</a>
</div>
```

### [尺寸](meta.md#sizes)

更改中繼資料的大小。

```html
<div class="ts-meta is-small">
    <a class="item">朝武芳乃</a>
    <a class="item">常陸茉子</a>
    <a class="item">ムラサメ</a>
</div>
<div class="ts-meta">
    <a class="item">朝武芳乃</a>
    <a class="item">常陸茉子</a>
    <a class="item">ムラサメ</a>
</div>
<div class="ts-meta is-large">
    <a class="item">朝武芳乃</a>
    <a class="item">常陸茉子</a>
    <a class="item">ムラサメ</a>
</div>
```

## 組合應用

### [標題與資料](meta.md#composition-header)

在部落格或是一些文章列表中，經常能看到其標題底下會有一個中繼資料的區塊。

```html
<div class="ts-header">野心更大的虛擬 YouTuber 團體邁向偶像化，而距離感也與日俱增</div>
<div class="ts-meta is-secondary">
    <a class="item">Yami Odymel</a>
    <a class="item">2020 年 02 月 14 日</a>
</div>
<div class="ts-divider is-section"></div>
<div class="ts-header">圖像複用、反轉、鏡射：怎麼將遊戲壓縮在 40 KB 以下還同時保持關卡獨特性？</div>
<div class="ts-meta is-secondary">
    <a class="item">Yami Odymel</a>
    <a class="item">2020 年 01 月 18 日</a>
</div>
```

在尋找相似的元件嗎？

- [清單](list.md)
