---
collection: tocas
version: "5.0.2"
title: "清單 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/5.0/zh-tw/list.html
fetched_at: 2025-03-22T01:53:10+08:00
---
```html
<div class="ts-list is-unordered">
    <div class="item">橙希</div>
    <div class="item">卡莉絲</div>
    <div class="item">羽田白音</div>
</div>
```

## 結構

### [巢狀式清單](list.md#sublist)

在項目裡面擺放一個清單可以達成巢狀式清單的結構。

```html
<div class="ts-list is-unordered">
    <div class="item">
        オルタナティブガールズ
        <div class="ts-list is-unordered">
            <div class="item">悠木美弥花</div>
            <div class="item">柊つむぎ</div>
            <div class="item">朝比奈乃々</div>
        </div>
    </div>
</div>
```

## 外觀

### [無序的](list.md#unordered)

沒有順序的排列項目，每個項目前面都會有一個黑點。

```html
<div class="ts-list is-unordered">
    <div class="item">七波白音</div>
    <div class="item">宮風夕梨</div>
    <div class="item">紬木沙羅</div>
</div>
```

### [有序的](list.md#ordered)

項目前都會有一個數字作為順序。

```html
<div class="ts-list is-ordered">
    <div class="item">伊波咲</div>
    <div class="item">栗宮希實</div>
    <div class="item">詩羽</div>
</div>
```

### [尺寸](list.md#sizes)

更改清單的大小。

```html
<div class="ts-list is-small is-unordered">
    <div class="item">箒木日向子</div>
    <div class="item">大舘流花</div>
    <div class="item">海蔵もも</div>
</div>
<div class="ts-list is-unordered">
    <div class="item">箒木日向子</div>
    <div class="item">大舘流花</div>
    <div class="item">海蔵もも</div>
</div>
<div class="ts-list is-large is-unordered">
    <div class="item">箒木日向子</div>
    <div class="item">大舘流花</div>
    <div class="item">海蔵もも</div>
</div>
```

## 樣式變數

|  | 說明 | 預設值 | 目標 |
| --- | --- | --- | --- |
| --gap | 項目之間的空白間隙高度。 | `0rem` | `.ts-list` |

在尋找相似的元件嗎？

- [中繼資料](meta.md)
