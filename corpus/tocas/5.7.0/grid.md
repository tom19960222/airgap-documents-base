---
collection: tocas
version: "5.7.0"
title: "網格系統 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/ef8248b165f458215fb8f18bb400c4bfba1767fa/docs/5.7/zh-tw/grid.html
fetched_at: 2026-02-25T00:25:36+08:00
---
```html
<div class="ts-grid">
    <div class="column is-4-wide"></div>
    <div class="column is-4-wide"></div>
    <div class="column is-4-wide"></div>
    <div class="column is-4-wide"></div>
</div>
```

## 概念

### [欄位與寬度](grid.md#wides)

網格系統每行為 16 格寬。欄位的寬度可以自行決定，沒有指定寬度的欄位會以其內容寬度為主。

這個範例由 2、8、6 格寬的欄位所組成，而 `2 + 8 + 6 = 16` 剛好達到了一行的最大格數。

```html
<div class="ts-grid">
    <div class="column is-2-wide"></div>
    <div class="column is-8-wide"></div>
    <div class="column is-6-wide"></div>
</div>
```

### [欄位換行](grid.md#wrapping)

如果單行的欄位寬度加起來超過 16 格寬，溢出來的欄位會自動換行。

這個範例由 5、6、8 格寬的欄位所組成，所以 `5 + 6 + 8 = 19`，多出來的欄位會換行。

```html
<div class="ts-grid">
    <div class="column is-5-wide"></div>
    <div class="column is-6-wide"></div>
    <div class="column is-8-wide"></div>
</div>
```

### [欄位數量](grid.md#amounts)

透過 `is-1-columns` 到 `is-10-columns` 指定單行要有幾個欄位，避免某些欄位沒辦法被 16 整除。

```html
<div class="ts-grid is-3-columns">
    <div class="column"></div>
    <div class="column"></div>
    <div class="column"></div>
</div>
<div class="ts-grid is-6-columns">
    <div class="column"></div>
    <div class="column"></div>
    <div class="column"></div>
    <div class="column"></div>
    <div class="column"></div>
    <div class="column"></div>
</div>
```

### [欄位均分](grid.md#evenly-divided)

每個欄位都有相同寬度，舉例來說：2 個欄位會各佔 50%，而 3 個欄位會均分成 33%…以此類推。

```html
<div class="ts-grid is-evenly-divided">
    <div class="column"></div>
    <div class="column"></div>
    <div class="column"></div>
</div>
```

### [巢狀式網格](grid.md#sub-grid)

網格系統內還可以有另一個網格系統。

```html
<div class="ts-grid is-2-columns">
    <div class="column">
        <div class="ts-grid is-4-columns">
            <div class="column"></div>
            <div class="column"></div>
            <div class="column"></div>
            <div class="column"></div>
        </div>
    </div>
    <div class="column"></div>
</div>
```

## 欄位

### [流動寬度](grid.md#fluid)

使某個欄位的寬度填滿剩餘空白位置。

```html
<div class="ts-grid">
    <div class="column is-4-wide"></div>
    <div class="column is-fluid"></div>
    <div class="column is-4-wide"></div>
</div>
```

### [移至首位、尾端](grid.md#first-and-last)

把某個欄位的排序調到第一個或是最後一個。

```html
<div class="ts-grid">
    <div class="column is-4-wide"></div>
    <div class="column is-4-wide"></div>
    <div class="column is-8-wide is-first"></div>
</div>
<div class="ts-grid">
    <div class="column is-8-wide is-last"></div>
    <div class="column is-4-wide"></div>
    <div class="column is-4-wide"></div>
</div>
```

### [指定順序](grid.md#orders)

透過 `is-order-1` 到 `is-order-10` 重新排序欄位，使用此功能時所有的欄位都必須指定順序。適合搭配[響應式設計](responsive.md)來在行動裝置上重新排序欄位。

```html
<div class="ts-grid">
    <div class="column is-2-wide is-order-4"></div>
    <div class="column is-3-wide is-order-3"></div>
    <div class="column is-4-wide is-order-2"></div>
    <div class="column is-7-wide is-order-1"></div>
</div>
```

## 外觀

### [水平對齊](grid.md#horizontal-aligns)

項目可以選擇靠左、中或右對齊。

```html
<div class="ts-grid is-start-aligned">
    <div class="column is-3-wide"></div>
    <div class="column is-3-wide"></div>
    <div class="column is-3-wide"></div>
</div>
<div class="ts-grid is-center-aligned">
    <div class="column is-3-wide"></div>
    <div class="column is-3-wide"></div>
    <div class="column is-3-wide"></div>
</div>
<div class="ts-grid is-end-aligned">
    <div class="column is-3-wide"></div>
    <div class="column is-3-wide"></div>
    <div class="column is-3-wide"></div>
</div>
```

### [垂直對齊](grid.md#vertical-aligns)

可以根據項目之間的高度，更改其上、中或下對齊方式。

```html
<div class="ts-grid is-top-aligned is-3-columns">
    <div class="column"></div>
    <div class="column"></div>
    <div class="column"></div>
</div>
<div class="ts-grid is-middle-aligned is-3-columns">
    <div class="column"></div>
    <div class="column"></div>
    <div class="column"></div>
</div>
<div class="ts-grid is-bottom-aligned is-3-columns">
    <div class="column"></div>
    <div class="column"></div>
    <div class="column"></div>
</div>
```

### [高度拉伸的](grid.md#stretched)

使欄位裡的[箱型容器](box.md)或第一層的元素高度拉伸至與其他欄位相同。

```html
<div class="ts-grid is-stretched is-3-columns">
    <div class="column">
        <div class="ts-box">
            <div class="ts-content">
                <p>這個片段有一行文字。</p>
            </div>
        </div>
    </div>
    <div class="column">
        <div class="ts-box">
            <div class="ts-content">
                <p>這個片段有兩行文字。</p>
                <p>這個片段有兩行文字。</p>
            </div>
        </div>
    </div>
    <div class="column">
        <div class="ts-box">
            <div class="ts-content">
                <p>這個片段有三行文字。</p>
                <p>這個片段有三行文字。</p>
                <p>每個片段高度都一樣。</p>
            </div>
        </div>
    </div>
</div>
```

### [分隔的](grid.md#divided)

讓欄位之間有垂直分隔線區隔項目，僅適用於單行的網格系統。

```html
<div class="ts-grid is-divided is-3-columns">
    <div class="column"></div>
    <div class="column"></div>
    <div class="column"></div>
</div>
```

### [空白圍繞](grid.md#space-between-and-around)

使空白圍繞在欄位之間或是周圍。

```html
<div class="ts-grid is-spaced-between">
    <div class="column is-3-wide"></div>
    <div class="column is-3-wide"></div>
    <div class="column is-3-wide"></div>
</div>
<div class="ts-grid is-spaced-around">
    <div class="column is-3-wide"></div>
    <div class="column is-3-wide"></div>
    <div class="column is-3-wide"></div>
</div>
```

### [顛倒順序](grid.md#reversed)

顛倒網格系統裡所有欄位順序，適合搭配[響應式設計](responsive.md)來在行動裝置上使用這個樣式。

```html
<div class="ts-grid is-reversed">
    <div class="column is-2-wide"></div>
    <div class="column is-4-wide"></div>
    <div class="column is-10-wide"></div>
</div>
```

### [層疊的](grid.md#stacked)

所有欄位會被迫獨立成為一行（便是將所有欄位設置為 16 格寬），適合搭配[響應式設計](responsive.md)在行動裝置上讓所有欄位層疊起來。

```html
<div class="ts-grid is-stacked">
    <div class="column is-2-wide"></div>
    <div class="column is-3-wide"></div>
    <div class="column is-4-wide"></div>
</div>
```

### [密度](grid.md#density)

網格系統裡欄位的間距可以更密或是更寬鬆。

```html
<div class="ts-grid is-relaxed is-3-columns">
    <div class="column"></div>
    <div class="column"></div>
    <div class="column"></div>
</div>
<div class="ts-grid is-3-columns">
    <div class="column"></div>
    <div class="column"></div>
    <div class="column"></div>
</div>
<div class="ts-grid is-compact is-3-columns">
    <div class="column"></div>
    <div class="column"></div>
    <div class="column"></div>
</div>
```

## 響應式設計

在 Tocas UI 裡，所有東西都可以套用[響應式設計](responsive.md)，下列範例僅作為基本的指導教學。

### [指定寬度](grid.md#responsive-wides)

欄位所佔的格數寬度可以依據裝置而有所不同，舉例來說：`tablet+:is-8-wide` 會在平板或更大的裝置上以 8 格寬的方式呈現。

```html
<div class="ts-grid">
    <div class="column mobile:is-16-wide tablet+:is-8-wide"></div>
    <div class="column mobile:is-16-wide tablet+:is-8-wide"></div>
    <div class="column mobile:is-16-wide tablet+:is-8-wide"></div>
    <div class="column mobile:is-16-wide tablet+:is-8-wide"></div>
</div>
```

### [自動層疊](grid.md#responsive-stacked)

在手機裝置時套用 `is-stacked` 層疊樣式就能讓所有欄位被迫獨立成為一行（便是將所有欄位設置為 16 格寬）。

```html
<div class="ts-grid mobile:is-stacked">
    <div class="column is-4-wide"></div>
    <div class="column is-4-wide"></div>
    <div class="column is-4-wide"></div>
    <div class="column is-4-wide"></div>
</div>
```

### [指定數量](grid.md#responsive-amounts)

在指定裝置上變更一個網格系統的欄位數量，這個範例的 `mobile:is-2-columns` 表示行動裝置會有 2 欄，而 `tablet+:is-3-columns` 是指平板或是更大的裝置會有 3 欄。

```html
<div class="ts-grid mobile:is-2-columns tablet+:is-3-columns">
    <div class="column"></div>
    <div class="column"></div>
    <div class="column"></div>
    <div class="column"></div>
    <div class="column"></div>
    <div class="column"></div>
</div>
```

### [可見度](grid.md#responsive-visibility)

某些欄位可以只在指定介面尺寸上出現、隱藏，相關使用方式請參閱[響應式設計](responsive.md)頁面。

```html
<div class="ts-grid">
    <div class="column mobile:has-hidden is-4-wide"></div>
    <div class="column tablet+:has-hidden is-4-wide"></div>
    <div class="column desktop-:has-hidden is-4-wide"></div>
    <div class="column widescreen:has-hidden is-4-wide"></div>
</div>
```

## 組合應用

### [搜尋列](grid.md#composition-search)

通常搜尋列會有流動欄位與固定欄位，沒有指定寬度的欄位會以其內容寬度為主。

```html
<div class="ts-grid">
    <div class="column is-fluid">
        <div class="ts-input">
            <input type="text" class="input" placeholder="搜尋文章…">
        </div>
    </div>
    <div class="column">
        <button class="ts-button">送出</button>
    </div>
</div>
```

## 樣式變數

|  | 說明 | 預設值 | 目標 |
| --- | --- | --- | --- |
| --gap | 欄位之間的空白間隙寬度。 | `1rem` | `.ts-grid` |

在尋找相似的元件嗎？

- [間隔容器](wrap.md)
