---
collection: tocas
version: "5.0.2"
title: "輸入欄位 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/5.0/zh-tw/field.html
fetched_at: 2025-03-22T01:53:10+08:00
---
```html
<div class="ts-field">
    <input type="text" placeholder="麥片、甜甜圈…">
    <label>關鍵字</label>
</div>
```

## 狀態

### [停用的](field.md#disabled)

使輸入欄位呈現無法互動、點擊的模樣。

```html
<div class="ts-field">
    <input type="text" placeholder="麥片、甜甜圈…" disabled>
    <label>關鍵字</label>
</div>
```

## 外觀

### [實心填充的](field.md#solid)

帶有實心背景的輸入欄位能更明確地呈現這是可供互動的元素。

```html
<div class="ts-field is-solid">
    <input type="text" placeholder="麥片、甜甜圈…">
    <label>關鍵字</label>
</div>
```

### [底線的](field.md#underlined)

以實心背景和底線明顯呈現一個輸入欄位，讓使用者如填寫表單一樣。

```html
<div class="ts-field is-underlined">
    <input type="text" placeholder="麥片、甜甜圈…">
    <label>關鍵字</label>
</div>
```

### [底線的](field.md#underlined)

以實心背景和底線明顯呈現一個輸入欄位，讓使用者如填寫表單一樣。

```html
<div class="ts-field is-border-labeled">
    <label>關鍵字</label>
    <input type="text" placeholder="麥片、甜甜圈…">
</div>
```

### [可調整尺寸的](field.md#resizable)

使用者可以拖曳角落邊緣，調整多行輸入欄位的高度。

```html
<div class="ts-field is-resizable">
    <textarea placeholder="回覆此訊息…"></textarea>
    <label>關鍵字</label>
</div>
<br>
<div class="ts-field is-resizable is-border-labeled">
    <textarea placeholder="回覆此訊息…"></textarea>
    <label>關鍵字</label>
</div>
```

### [帶標籤的](field.md#labeled)

輸入欄位的開頭或結束位置可以擺放文字標籤，作為前輟或後輟提示。

```html
<div class="ts-input is-start-labeled">
    <span class="label">$</span>
    <input type="text">
</div>
<div class="ts-input is-labeled">
    <span class="label">https://</span>
    <input type="text">
    <span class="label">.co</span>
</div>
<div class="ts-input is-end-labeled">
    <input type="text">
    <span class="label">.00</span>
</div>
```

### [負面的](field.md#negative)

表示輸入欄位出錯，不符合表單驗證規則。

```html
<div class="ts-input is-negative">
    <input type="text" placeholder="電子信箱地址">
</div>
```

### [側邊圖示](field.md#side-icon)

欄位的左右兩側可以擺放輔助圖示。

```html
<div class="ts-input is-start-icon">
    <span class="ts-icon is-phone-icon"></span>
    <input type="text" placeholder="電話號碼">
</div>
<div class="ts-input is-icon">
    <span class="ts-icon is-phone-icon"></span>
    <input type="text" placeholder="電話號碼">
    <span class="ts-icon is-triangle-exclamation-icon"></span>
</div>
<div class="ts-input is-end-icon">
    <input type="text" placeholder="密碼">
    <span class="ts-icon is-lock-icon"></span>
</div>
```

### [尺寸](field.md#sizes)

更改輸入欄位的大小。

```html
<div class="ts-input is-small">
    <input type="text" placeholder="小型輸入欄位">
</div>
<div class="ts-input">
    <input type="text" placeholder="預設輸入欄位">
</div>
<div class="ts-input is-large">
    <input type="text" placeholder="大型輸入欄位">
</div>
```

### [密度](field.md#density)

變更輸入欄位的高度，看起來更緊密或是令人感到寬鬆。

```html
<div class="ts-input is-dense">
    <input type="text" placeholder="緊密欄位">
</div>
<div class="ts-input">
    <input type="text" placeholder="預設欄位">
</div>
<div class="ts-input is-relaxed">
    <input type="text" placeholder="寬鬆欄位">
</div>
```

## 種類

### [顏色選擇器](field.md#type-color)

透過原生的輸入欄位選擇指定的顏色。

```html
<div class="ts-input">
    <input type="color">
</div>
```

### [日期與時間](field.md#date-and-time)

HTML 有提供數種用於時間、日期與週期的輸入欄位。

```html
<div class="ts-input">
    <input type="datetime-local">
</div>
<div class="ts-input">
    <input type="date">
</div>
<div class="ts-input">
    <input type="time">
</div>
<div class="ts-input">
    <input type="month">
</div>
<div class="ts-input">
    <input type="week">
</div>
```
