---
collection: tocas
version: "5.0.2"
title: "檔案上傳 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/5.0/zh-tw/file.html
fetched_at: 2025-03-22T01:53:10+08:00
---
```html
<div class="ts-file">
    <input type="file">
</div>
```

## 狀態

### [停用的](file.md#disabled)

使檔案欄位呈現無法互動、點擊的模樣。

```html
<div class="ts-file">
    <input type="file" disabled>
</div>
```

## 外觀

### [實心填充的](file.md#solid)

帶有實心背景的欄位能更明確地呈現這是可供互動的元素。

```html
<div class="ts-file is-solid">
    <input type="file">
</div>
```

### [底線的](file.md#underlined)

以實心背景和底線明顯呈現一個欄位，讓使用者如填寫表單一樣。

```html
<div class="ts-file is-underlined">
    <input type="file">
</div>
```

### [負面的](file.md#negative)

令一個欄位看起來帶有負面或危險的狀態，通常可能是指這個欄位沒有選擇檔案。

```html
<div class="ts-file is-negative">
    <input type="file">
</div>
```

### [尺寸](file.md#sizes)

更改檔案上傳的尺寸與文字大小。

```html
<div class="ts-file is-small">
    <input type="file">
</div>
<div class="ts-file">
    <input type="file">
</div>
<div class="ts-file is-large">
    <input type="file">
</div>
```

### [密度](file.md#density)

變更檔案上傳的高度，看起來更緊密或是令人感到寬鬆。

```html
<div class="ts-file is-dense">
    <input type="file">
</div>
<div class="ts-file">
    <input type="file">
</div>
<div class="ts-file is-relaxed">
    <input type="file">
</div>
```
