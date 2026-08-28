---
collection: tocas
version: "5.0.2"
title: "下拉式選擇 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/5.0/zh-tw/select.html
fetched_at: 2025-03-22T01:53:10+08:00
---
```html
<div class="ts-select">
    <select>
        <option>蘋果</option>
        <option>西瓜</option>
        <option>香蕉</option>
    </select>
</div>
```

## 種類

### [多選的](select.md#multiple)

下拉選擇欄位支援 HTML 原生的 `[multiple]` 多選屬性。

```html
<div class="ts-select">
    <select size="3" multiple>
        <option>項目 A</option>
        <option>項目 B</option>
        <option>項目 C</option>
    </select>
</div>
```

## 狀態

### [停用的](select.md#disabled)

使下拉選擇欄位呈現無法互動、點擊的模樣。

```html
<div class="ts-select">
    <select disabled>
        <option>MySpace</option>
        <option>Facebook</option>
        <option>Twitter</option>
    </select>
</div>
```

### [啟用的](select.md#active)

表示選擇欄位目前正在被選取或是展開的樣子。

```html
<div class="ts-select is-active">
    <select>
        <option>TeaMeow</option>
        <option>Tunalog</option>
        <option>EnekoCore</option>
    </select>
</div>
```

## 外觀

### [實心填充的](select.md#solid)

帶有實心背景的欄位能更明確地呈現這是可供互動的元素。

```html
<div class="ts-select is-solid">
    <select>
        <option>Golang</option>
        <option>PHP</option>
        <option>Node.js</option>
    </select>
</div>
```

### [底線的](select.md#underlined)

以實心背景和底線明顯呈現一個欄位，讓使用者如填寫表單一樣。

```html
<div class="ts-select is-underlined">
    <select>
        <option>台東</option>
        <option>高雄</option>
        <option>台南</option>
    </select>
</div>
```

### [基本的](select.md#basic)

移除所有多餘的結構，僅呈現下拉文字與輔助圖示。

```html
<div class="ts-select is-basic">
    <select>
        <option>AMD</option>
        <option>Intel</option>
    </select>
</div>
```

### [負面的](select.md#negative)

令一個欄位看起來帶有負面或危險的狀態，通常可能是指這個欄位沒有被選擇。

```html
<div class="ts-select is-negative">
    <select>
        <option>Yami Odymel</option>
        <option>Mac Taylor</option>
        <option>Val Pyen</option>
    </select>
</div>
```

### [流動的](select.md#fluid)

使欄位的寬度符合父容器的寬度。

```html
<div class="ts-select is-fluid">
    <select>
        <option>千導院楓</option>
        <option>粒櫻杏子</option>
        <option>若葉昴</option>
    </select>
</div>
```

### [尺寸](select.md#sizes)

更改下拉式選擇的文字大小。

```html
<div class="ts-select is-small">
    <select>
        <option>小型欄位</option>
    </select>
</div>
<div class="ts-select">
    <select>
        <option>預設欄位</option>
    </select>
</div>
<div class="ts-select is-large">
    <select>
        <option>大型欄位</option>
    </select>
</div>
```

### [密度](select.md#density)

在不改變文字大小的情況下變更欄位的高度，看起來更緊密或是令人感到寬鬆。

```html
<div class="ts-select is-dense">
    <select>
        <option>緊密欄位</option>
    </select>
</div>
<div class="ts-space"></div>
<div class="ts-select">
    <select>
        <option>預設欄位</option>
    </select>
</div>
<div class="ts-space"></div>
<div class="ts-select is-relaxed">
    <select>
        <option>寬鬆欄位</option>
    </select>
</div>
```

在尋找相似的元件嗎？

- [彈出式選單](dropdown.md)
