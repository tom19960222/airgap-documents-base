---
collection: tocas
version: "5.0.2"
title: "頁數導覽列 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/5.0/zh-tw/pagination.html
fetched_at: 2025-03-22T01:53:10+08:00
---
```html
<div class="ts-pagination">
    <a class="item is-back"></a>
    <a class="item">1</a>
    <a class="item is-active">2</a>
    <a class="item">3</a>
    <a class="item">4</a>
    <a class="item is-next"></a>
</div>
```

## 狀態

### [啟用的](pagination.md#active)

表示目前檢視的頁數。

```html
<div class="ts-pagination">
    <a class="item">1</a>
    <a class="item is-active">2</a>
    <a class="item">3</a>
</div>
```

### [停用的](pagination.md#disabled)

使頁數呈現無法互動、點擊的模樣。若頁數是超連結，則需套用 `.is-disabled` 樣式。

```html
<div class="ts-pagination">
    <button class="item is-back" disabled>上一頁</button>
    <a class="item is-active">1</a>
    <a class="item">2</a>
    <a class="item">3</a>
    <a class="item is-next is-disabled">下一頁</a>
</div>
```

## 項目

### [上、下一頁](pagination.md#previous-and-next)

帶有前、後圖示的項目，能夠同時在裡面擺放文字。

```html
<div class="ts-pagination">
    <a class="item is-back">上一頁</a>
    <a class="item">1</a>
    <a class="item">2</a>
    <a class="item">3</a>
    <a class="item is-next">下一頁</a>
</div>
```

### [第一頁、最後頁](pagination.md#first-and-last)

帶有最新、最舊圖示的項目，能夠導引使用者到第一頁或最後一頁，能夠同時在裡面擺放文字。

```html
<div class="ts-pagination">
    <a class="item is-first">最新</a>
    <a class="item">1</a>
    <a class="item">2</a>
    <a class="item">3</a>
    <a class="item is-last">最舊</a>
</div>
```

### [省略的](pagination.md#skipped)

用省略符號表示某些頁數不重要，避免佔空間。

```html
<div class="ts-pagination">
    <a class="item">1</a>
    <span class="item is-skipped"></span>
    <a class="item">4</a>
    <a class="item is-active">5</a>
    <a class="item">6</a>
    <span class="item is-skipped"></span>
    <a class="item">10</a>
</div>
```

## 外觀

### [次要的](pagination.md#secondary)

讓整個導覽列沒那麼顯眼。

```html
<div class="ts-pagination is-secondary">
    <a class="item is-back"></a>
    <a class="item">1</a>
    <a class="item is-skipped"></a>
    <a class="item">4</a>
    <a class="item is-active">5</a>
    <a class="item">6</a>
    <a class="item is-skipped"></a>
    <a class="item">10</a>
    <a class="item is-next"></a>
</div>
```

### [外框線的](pagination.md#outlined)

以外框線襯托每個頁數項目。

```html
<div class="ts-pagination is-outlined">
    <a class="item is-back"></a>
    <a class="item">1</a>
    <a class="item is-active">2</a>
    <a class="item">3</a>
    <a class="item is-next"></a>
</div>
```

### [流動的](pagination.md#fluid)

令整個頁數導覽列和父容器有相同的寬度。

```html
<div class="ts-pagination is-fluid">
    <a class="item is-back"></a>
    <a class="item">1</a>
    <a class="item">2</a>
    <a class="item">3</a>
    <a class="item is-next"></a>
</div>
```

### [尺寸](pagination.md#sizes)

更改頁數導覽列的大小。

```html
<div class="ts-pagination is-small">
    <a class="item is-back"></a>
    <a class="item">1</a>
    <a class="item is-active">2</a>
    <a class="item">3</a>
    <a class="item is-next"></a>
</div>
<div class="ts-pagination">
    <a class="item is-back"></a>
    <a class="item">1</a>
    <a class="item is-active">2</a>
    <a class="item">3</a>
    <a class="item is-next"></a>
</div>
<div class="ts-pagination is-large">
    <a class="item is-back"></a>
    <a class="item">1</a>
    <a class="item is-active">2</a>
    <a class="item">3</a>
    <a class="item is-next"></a>
</div>
```

### [寬鬆的](pagination.md#relaxed)

使項目之間看起來更寬鬆不擁擠。

```html
<div class="ts-pagination is-outlined">
    <a class="item is-back"></a>
    <a class="item">1</a>
    <a class="item is-active">2</a>
    <a class="item">3</a>
    <a class="item is-next"></a>
</div>
<div class="ts-pagination is-outlined is-relaxed">
    <a class="item is-back"></a>
    <a class="item">1</a>
    <a class="item is-active">2</a>
    <a class="item">3</a>
    <a class="item is-next"></a>
</div>
```

### [較密的](pagination.md#dense)

變更元件的內距，令元素之間看起來更密集。

```html
<div class="ts-pagination is-dense">
    <a class="item is-back"></a>
    <a class="item">1</a>
    <a class="item is-active">2</a>
    <a class="item">3</a>
    <a class="item is-next"></a>
</div>
```

## 組合應用

### [詳細分頁列](pagination.md#composition-detail)

在資料的上、下方通常會有一個換頁用的導覽列，有時會包含筆數資訊。

```html
<div class="ts-box">
    <table class="ts-table is-basic">
        <thead>
            <tr>
                <th>醫院種類</th>
                <th>名稱</th>
                <th class="is-collapsed">建立於</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="is-collapsed">東京 AH 綜合醫院</td>
                <td>醫學藥品</td>
                <td>2021/08/01</td>
            </tr>
            <tr>
                <td class="is-collapsed">東京 AH 綜合醫院</td>
                <td>常規心電圖</td>
                <td>2021/08/01</td>
            </tr>
        </tbody>
    </table>
    <div class="ts-divider"></div>
    <div class="ts-content is-dense is-secondary">
        <div class="ts-grid is-middle-aligned">
            <div class="column is-fluid">
                單頁筆數：
                <div class="ts-select is-basic">
                    <select>
                        <option>10</option>
                        <option>20</option>
                        <option selected>30</option>
                    </select>
                </div>
            </div>
            <div class="column">
                <div class="ts-pagination is-secondary">
                    <a class="item is-back"></a>
                    <a class="item">1</a>
                    <a class="item is-skipped"></a>
                    <a class="item">4</a>
                    <a class="item is-active">5</a>
                    <a class="item">6</a>
                    <a class="item is-skipped"></a>
                    <a class="item">10</a>
                    <a class="item is-next"></a>
                </div>
            </div>
        </div>
    </div>
</div>
```
